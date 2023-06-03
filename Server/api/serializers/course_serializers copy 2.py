from rest_framework import serializers
from courses.models import *
from django.contrib.auth.models import User
from taggit.serializers import TagListSerializerField, TaggitSerializer
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from api.utils import make_slug
from rest_framework.fields import Field
import json, collections
from django.core.serializers.json import DjangoJSONEncoder


class GenericRelatedField(Field):
    """
    A custom field that expect object URL as input and transforms it
    to django model instance.
    """
    read_only = False

    def __init__(self, related_models=(), **kwargs):
        super(GenericRelatedField, self).__init__(**kwargs)
        # related models - list of models that should be acceptable by 
        # field. Note that all this models should have corresponding 
        # endpoint.
        self.related_models = related_models
        self._default_view_name = ""

    def to_representation(self, obj):
        """ Serializes any object to its URL representation """
        repr = {}
        
        match obj.__class__.__name__:
            case Text.__name__:
                repr['content'] = obj.content
            case Code.__name__:
                repr['content'] = obj.content
                repr['language'] = obj.language
        
        return repr

class LessonContentSerializer(serializers.ModelSerializer):
    item = GenericRelatedField(related_models=(Text, Code, Image, File), read_only=True)
    
    class Meta:
        model = LessonContent
        fields = ('id', 'order', 'item')
    
    def is_valid(self, *, raise_exception=False):
        if self.context.get('request').method == 'POST':
            return super().is_valid()
        if self.context.get('request').method == 'GET':
        
            self._errors = {}
            data = self.initial_data
            if data.get("_state", None):
                del data['_state']
            data['item'] = LessonContent.objects.get(object_id=data['object_id'])
            self._validated_data = collections.OrderedDict(data)
            # print(self._validated_data)
            return True

    def save(self):
        if self.context.get('request').method == 'POST':
            print(self.initial_data)
            print(self.validated_data)
            return super().save()
        elif self.context.get('request').method == 'GET':
            if self.instance is not None:
                self.instance = self.update(self.instance, self._validated_data)
                assert self.instance is not None, (
                    '`update()` did not return an object instance.'
                )
            else:
                self.instance = self.create(self._validated_data)
                assert self.instance is not None, (
                    '`create()` did not return an object instance.'
                )
            return self.instance

class LessonSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    # subchapter = serializers.PrimaryKeyRelatedField(required=False, queryset=Subchapter.objects.all())
    slug = serializers.SlugField(read_only=True)
    lesson_contents = LessonContentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Lesson
        fields = ("id", "theme", "slug", "order", "lesson_contents")
    
    def to_representation(self, instance):
        lesson_content = LessonContent.objects.filter(lesson__pk=instance.pk).\
            order_by('order')
        l_c_objects = []
        for l_c in lesson_content:
            data = l_c.__dict__
            ser = LessonContentSerializer(data=data)
            if ser.is_valid(raise_exception=True):
                # print(ser.validated_data)
                ser.save()
            else:
                print(ser.errors)
            l_c_objects.append(ser)
        
        r = super().to_representation(instance)
        print(r)
        print(l_c_objects)
        
        return r | {"lesson_contents": l_c_objects}
    
    def create(self, validated_data):
        validated_data['slug'] = make_slug(validated_data['theme'])
        return super().create(validated_data)

class SubchapterSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    # chapter = serializers.PrimaryKeyRelatedField(required=False, queryset=Chapter.objects.all())
    lessons = LessonSerializer(many=True, read_only=True)
    
    class Meta:
        model = Subchapter
        fields = ("id", "title", "order", "lessons")

class ChapterSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    subchapters = SubchapterSerializer(many=True, read_only=True)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), required=False)
    
    class Meta:
        model = Chapter
        fields = ("id", "title", "course", "order", "subchapters")



class CourseSerializer(TaggitSerializer, serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ('owners', 'created', 'updated', 'visibility')
        # fields = ('chapters', 'slug', 'title', 'description', 'tags', 'header_photo')
    
    tags = TagListSerializerField()
    header_photo = serializers.ImageField(required=False, max_length=None, allow_empty_file=False, allow_null=False, use_url=True)
    description = serializers.CharField(required=False)
    chapters = ChapterSerializer(many=True, read_only=True)
    
    def create(self, validated_data):
        validated_data['slug'] = make_slug(validated_data['title'])
        instance = super().create(validated_data)
        instance.owners.add(self.context.get('request').user)
        instance.save()
        
        return instance
    
    def update(self, instance, validated_data):
        if 'title' in validated_data.keys():
            validated_data['slug'] = make_slug(validated_data['title'])
        return super().update(instance, validated_data)