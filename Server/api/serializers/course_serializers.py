from rest_framework import serializers
from edit_course_zone.models import *
from django.contrib.auth.models import User
from taggit.serializers import TagListSerializerField, TaggitSerializer
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from api.utils import make_slug
from django.urls import resolve, Resolver404
from rest_framework.fields import Field
import json, collections
from django.core.serializers.json import DjangoJSONEncoder


class GenericRelatedField(Field):
    """
    A custom field that expect object URL as input and transforms it
    to django model instance.
    """
    read_only = False
    _default_view_name = '%(model_name)s-detail'
    lookup_field = 'pk'

    def __init__(self, related_models=(), **kwargs):
        super(GenericRelatedField, self).__init__(**kwargs)
        # related models - list of models that should be acceptable by 
        # field. Note that all this models should have corresponding 
        # endpoint.
        self.related_models = related_models

    def _get_url_basename(self, obj):
        """ Get object URL basename """
        format_kwargs = {
            'app_label': obj._meta.app_label,
            'model_name': obj._meta.object_name.lower()
        }
        return self._default_view_name % format_kwargs

    def _get_request(self):
        try:
            return self.context['request']
        except KeyError:
            raise AttributeError('GenericRelatedField have to be initialized with `request` in context')

    def to_representation(self, obj):
        """ Serializes any object to its URL representation """
        # kwargs = {self.lookup_field: getattr(obj, self.lookup_field)}
        # request = self._get_request()
        # return super().to_representation(obj)
        # return request.build_absolute_uri(reverse(self._get_url_basename(obj), kwargs=kwargs))
        return obj.pk

    def clear_url(self, url):
        """ Removes domain and protocol from url """
        if url.startswith('http'):
             return '/' + url.split('/', 3)[-1]
        return url

    def get_model_from_resolve_match(self, match):
        queryset = match.func.cls.queryset
        if queryset is not None:
            return queryset.model
        else:
            return match.func.cls.model

    def instance_from_url(self, url):
        url = self.clear_url(url)
        match = resolve(url)
        model = self.get_model_from_resolve_match(match)
        return model.objects.get(**match.kwargs)

    def to_internal_value(self, data):
        """ Restores model instance from its URL """
        if not data:
            return None
        request = self._get_request()
        user = request.user
        try:
            obj = self.instance_from_url(data)
            model = obj.__class__
        except (Resolver404, AttributeError, MultipleObjectsReturned, ObjectDoesNotExist):
            raise serializers.ValidationError("Can`t restore object from url: %s" % data)
        if model not in self.related_models:
            raise serializers.ValidationError('%s object does not support such relationship' % str(obj))
        return obj


class LessonContentSerializer(serializers.ModelSerializer):
    item = GenericRelatedField(related_models=(Text, Code, Image, File), read_only=True)
    
    class Meta:
        model = LessonContent
        fields = ('id', 'order', 'item')

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
            order_by('order').values()
        s = LessonContentSerializer(data=lesson_content[0])
        if s.is_valid():
            print(s.validated_data)
        qs_json = [collections.OrderedDict(o) for o in lesson_content]
        # print(qs_json)
        r = super().to_representation(instance)
        # r["lesson_contents"] = json.dumps([LessonContentSerializer(data=o) for o in lesson_content], cls=DjangoJSONEncoder)
        # print(qs_json)
        
        return r | {"lesson_contents": qs_json}
    
    def create(self, validated_data):
        validated_data['slug'] = make_slug(validated_data['title'])
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