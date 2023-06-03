from rest_framework import serializers, validators
from edit_course_zone.models import *
from django.contrib.auth.models import User
from taggit.serializers import TagListSerializerField, TaggitSerializer
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from api.utils import make_slug
from rest_framework.fields import Field
import json, collections
from django.core.serializers.json import DjangoJSONEncoder
from api.constants import AVAILABLE_LESSON_CONTENT_MODELS


class LessonContentRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value, AVAILABLE_LESSON_CONTENT_MODELS):
            return {"content_type": value._meta.model_name} | \
                { field.name : getattr(value, field.name) for field in value._meta.fields }
        return super().to_representation(value)

class LessonContentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    item = LessonContentRelatedField(read_only=True)
    
    class Meta:
        model = LessonContent
        fields = "__all__"
    
    def validate(self, attrs):
        if self.context.get("model_instance"):
            m_i = getattr(self.context.get("model_instance"), "url").lower()
            if "youtube.com" not in m_i or "?w" not in m_i:
                raise validators.ValidationError("Укажите ссылку на YouTube")
        return super().validate(attrs)

class LessonContentGETSerializer(LessonContentSerializer):
    def create(self, validated_data):
        return self.Meta.model.objects.get(content_type=validated_data.get('content_type'),
                                           object_id=validated_data.get('object_id'))


class LessonSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    slug = serializers.SlugField(read_only=True)
    lesson_contents = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Lesson
        fields = ("id", "theme", "slug", "order", "lesson_contents")
    
    def get_lesson_contents(self, obj):
        lesson_content = LessonContent.objects.filter(lesson__pk=obj.pk)
        l_c_objects = []
        for l_c in lesson_content:
            data = l_c.__dict__
            data.update({'content_type': data.pop("content_type_id")})
            data.update({'lesson': data.pop("lesson_id")})
            ser = LessonContentGETSerializer(data=data)
            
            if ser.is_valid():
                ser.save()
            else:
                print(ser.errors)
            l_c_objects.append(ser.data)
        return l_c_objects
    
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

class CourseListSerializer(TaggitSerializer, serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ('owners', 'created', 'updated', 'visibility')
    
    tags = TagListSerializerField()
    header_photo = serializers.ImageField(required=False, max_length=None, allow_empty_file=False, allow_null=False, use_url=True)
    description = serializers.CharField(required=False)

class CourseParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseParticipant
        fields = "__all__"