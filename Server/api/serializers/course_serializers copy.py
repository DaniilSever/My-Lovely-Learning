from rest_framework import serializers
from courses.models import Course, Chapter, Subchapter, Lesson, LessonContent
from django.contrib.auth.models import User
from taggit.serializers import TagListSerializerField, TaggitSerializer
from django.core.exceptions import ObjectDoesNotExist
from api.utils import make_slug

class LessonContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonContent
        fields = ('order', 'item')

class LessonSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    subchapter = serializers.PrimaryKeyRelatedField(required=False, queryset=Subchapter.objects.all())
    slug = serializers.SlugField(read_only=True)
    # lesson_contents = LessonContentSerializer(many=True, required=False)
    
    class Meta:
        model = Lesson
        fields = "__all__"
    
    def create(self, validated_data):
        lesson_contents = validated_data.pop('lesson_contents') \
            if validated_data.get('lesson_contents', None) else None
        
        lesson = Lesson.objects.create(**validated_data)
        lesson.slug = make_slug(validated_data.get("theme"))
        lesson.save()
        
        if lesson_contents:
            for contents in lesson_contents:
                data = dict(contents)
                data['lesson'] = lesson
                print(f"[CREATE] Lesson data: {data}")
                # lesson_serializer = LessonSerializer(data=data)
                # if lesson_serializer.is_valid():
                #     lesson_serializer.save()
        
        return lesson
    
    def update(self, instance, validated_data):
        if instance.theme != validated_data.get("theme", None):
            instance.slug = make_slug(validated_data.get("theme"))
        instance.theme = validated_data.get("theme", instance.theme)
        instance.order = validated_data.get("order", instance.order)
        instance.save()
        
        lesson_contents = validated_data.pop('lesson_contents') \
            if validated_data.get('lesson_contents', None) else None
        
        return instance

class SubchapterSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    chapter = serializers.PrimaryKeyRelatedField(required=False, queryset=Chapter.objects.all())
    lessons = LessonSerializer(many=True, required=False)
    
    class Meta:
        model = Subchapter
        fields = "__all__"
    
    def create(self, validated_data):
        lessons = validated_data.pop('lessons') \
            if validated_data.get('lessons', None) else None
        
        subchapter = Subchapter.objects.create(**validated_data)
        
        if lessons:
            for lesson in lessons:
                data = dict(lesson)
                data['subchapter'] = subchapter.pk
                lesson_serializer = LessonSerializer(data=data)
                if lesson_serializer.is_valid():
                    lesson_serializer.save()
                else:
                    print(f"[CREATE] LessonSerializer errors: {lesson_serializer.errors}")
        
        return subchapter
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.order = validated_data.get("order", instance.order)
        instance.save()
        
        lessons = validated_data.pop('lessons') \
            if validated_data.get('lessons', None) else None
        
        if lessons:
            keep_lessons = []
            for lesson in lessons:
                if "id" in lesson.keys(): # существующий урок
                    try:
                        lesson_instance = Lesson.objects.get(id=lesson['id'])
                        data = {}
                        data['title'] = lesson.get("title", lesson_instance.title)
                        data['order'] = lesson.get("order", lesson_instance.order)
                        data['subchapter'] = validated_data.get("subchapter", lesson_instance.subchapter)
                        
                        lesson_serializer = LessonSerializer(lesson_instance, data=data)
                        if lesson_serializer.is_valid():
                            lesson_serializer.save()
                        else:
                            print(f"[UPDATE] ChapterSerializer errors: {lesson_serializer.errors}")
                        
                        keep_lessons.append(lesson_instance.id)
                    except ObjectDoesNotExist: continue
                else:
                    data = dict(lesson)
                    data['subchapter'] = instance.id
                    lesson_serializer = LessonSerializer(data=data)
                    if lesson_serializer.is_valid():
                            lesson_serializer.save()
                    else:
                        print(f"[CREATE-UPDATE] SubchapterSerializer errors: {lesson_serializer.errors}")
                    keep_lessons.append(lesson.id)
        
            for lesson in instance.lessons.all():
                if lesson.id not in keep_lessons:
                    lesson.delete()
            
            return instance

class ChapterSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    course = serializers.PrimaryKeyRelatedField(required=False, queryset=Course.objects.all())
    subchapters = SubchapterSerializer(many=True, required=False)
    
    class Meta:
        model = Chapter
        fields = "__all__"
    
    def create(self, validated_data):
        subchapters = validated_data.pop('subchapters') \
            if validated_data.get('subchapters', None) else None
        
        chapter = Chapter.objects.create(**validated_data)
        
        if subchapters:
            for subchapter in subchapters:
                data = dict(subchapter)
                data['chapter'] = chapter.pk
                subchapter_serializer = SubchapterSerializer(data=data)
                if subchapter_serializer.is_valid():
                    subchapter_serializer.save()
                else:
                    print(f"[CREATE] SubchapterSerializer errors: {subchapter_serializer.errors}")
        
        return chapter
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.order = validated_data.get("order", instance.order)
        instance.save()
        
        subchapters = validated_data.pop('subchapters') \
            if validated_data.get('subchapters', None) else None
        
        if subchapters:
            keep_subchapters = []
            for subchapter in subchapters:
                if "id" in subchapter.keys(): # существующий подраздел
                    try:
                        subchapter_instance = Subchapter.objects.get(id=subchapter['id'])
                        data = {}
                        data['title'] = subchapter.get("title", subchapter_instance.title)
                        data['order'] = subchapter.get("order", subchapter_instance.order)
                        data['chapter'] = validated_data.get("chapter", subchapter_instance.chapter)
                        
                        subchapter_serializer = SubchapterSerializer(subchapter_instance, data=data)
                        if subchapter_serializer.is_valid():
                            subchapter_serializer.save()
                        else:
                            print(f"[UPDATE] ChapterSerializer errors: {subchapter_serializer.errors}")
                        
                        keep_subchapters.append(subchapter_instance.id)
                    except ObjectDoesNotExist: continue
                else:
                    data = dict(subchapter)
                    data['chapter'] = instance.id
                    subchapter_serializer = SubchapterSerializer(data=data)
                    if subchapter_serializer.is_valid():
                            subchapter_serializer.save()
                    else:
                        print(f"[CREATE-UPDATE] SubchapterSerializer errors: {subchapter_serializer.errors}")
                    keep_subchapters.append(subchapter.id)
        
            for subchapter in instance.subchapters.all():
                if subchapter.id not in keep_subchapters:
                    subchapter.delete()
        
        return instance


class CourseSerializer(TaggitSerializer, serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
    
    tags = TagListSerializerField()
    header_photo = serializers.ImageField(required=False, max_length=None, allow_empty_file=False, allow_null=False, use_url=True)
    chapters = ChapterSerializer(many=True, required=False)
    description = serializers.CharField(required=False)
    
    def create(self, validated_data):
        to_be_tagged, validated_data = self._pop_tags(validated_data)
        
        chapters = validated_data.pop('chapters') \
            if validated_data.get('chapters', None) else None

        validated_data["slug"] = make_slug(validated_data["title"])
        if validated_data.get('owners', None):
            owners = validated_data.pop('owners')
        course = Course.objects.create(**validated_data)
        course.owners.add(self.context.get('request').user)
        course.save()
        
        if chapters:
            for chapter in chapters:
                data = dict(chapter)
                data['course'] = course.pk
                chapter_serializer = ChapterSerializer(data=data)
                if chapter_serializer.is_valid():
                    chapter_serializer.save()
        
        self._save_tags(course, to_be_tagged)
        
        return course
    
    def update(self, instance, validated_data):
        to_be_tagged, validated_data = self._pop_tags(validated_data)
        
        owners = instance.owners.all()
        new_owners = validated_data.get('owners', owners)
        
        if owners != new_owners:
            instance.owners.clear()
            for owner in new_owners:
                instance.owners.add(User.objects.get(id=owner.id))
        
        if instance.title != validated_data.get("title", None):
            instance.slug = make_slug(validated_data.get("title"))
        
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.header_photo = validated_data.get("header_photo", instance.header_photo)
        instance.visibility = validated_data.get("visibility", instance.visibility)
        instance.save()
        
        chapters = validated_data.pop('chapters') \
            if validated_data.get('chapters', None) else None
        
        if chapters:
            keep_chapters = []
            for chapter in chapters:
                if "id" in chapter.keys(): # существующая глава
                    try:
                        chapter_instance = Chapter.objects.get(id=chapter['id'])
                        data = {}
                        data['title'] = chapter.get("title", chapter_instance.title)
                        data['order'] = chapter.get("order", chapter_instance.order)
                        data['course'] = instance.id
                        
                        chapter_serializer = ChapterSerializer(chapter_instance, data=data)
                        if chapter_serializer.is_valid():
                            chapter_serializer.save()
                        else:
                            print(f"[UPDATE] ChapterSerializer errors: {chapter_serializer.errors}")
                        
                        keep_chapters.append(chapter_instance.id)
                    except ObjectDoesNotExist: continue
                else:
                    data = dict(chapter)
                    data['course'] = instance.id
                    chapter_serializer = ChapterSerializer(data=data)
                    if chapter_serializer.is_valid():
                        chapter_serializer.save()
                    else:
                        print(f"[CREATE-UPDATE] ChapterSerializer errors: {chapter_serializer.errors}")
                    keep_chapters.append(chapter.get('id'))
        
            for chapter in instance.chapters.all():
                if chapter.id not in keep_chapters:
                    chapter.delete()
        
        self._save_tags(instance, to_be_tagged)
        
        return instance