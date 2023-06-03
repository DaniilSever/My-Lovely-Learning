from rest_framework import generics, response, authentication, permissions, mixins
from edit_course_zone.models import Course
from api.serializers.course_serializers import *
from api.mixins import *
from rest_framework import status
from django.contrib.contenttypes.models import ContentType
from edit_course_zone.models import *

FORBIDDEN_RESPONSE = response.Response({"message": "Отказано в доступе"}, status=status.HTTP_403_FORBIDDEN)

class CreateCourse(CourseMixin, generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class DeleteCourse(CourseOwnerMixin, CourseMixin, generics.DestroyAPIView):
    lookup_field = 'pk'

class RetrieveUpdateCourse(CourseOwnerMixin, CourseMixin, generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'

class AddChapter(CourseOwnerMixin, ChapterMixin, generics.CreateAPIView):
    lookup_field = 'course_id'
    
    def post(self, request, *args, **kwargs):
        #TODO: любой может добавлять подразделы, исправить
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(course=Course.objects.get(pk=self.kwargs.get(self.lookup_field)))
            return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteChapter(CourseOwnerMixin, ChapterMixin, generics.DestroyAPIView):
    lookup_field = 'pk'

class RetrieveUpdateChapter(CourseOwnerMixin, ChapterMixin, generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'

class AddSubchapter(CourseOwnerMixin, SubchapterMixin, generics.CreateAPIView):
    lookup_field = 'chapter_id'
    
    def post(self, request, *args, **kwargs):
        #TODO: любой может добавлять подразделы, исправить
        print(self.kwargs)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(chapter=Chapter.objects.get(pk=self.kwargs.get(self.lookup_field)))
            return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteSubchapter(CourseOwnerMixin, SubchapterMixin, generics.DestroyAPIView):
    lookup_field = 'pk'

class RetrieveUpdateSubchapter(CourseOwnerMixin, SubchapterMixin, generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'

class AddLesson(CourseOwnerMixin, LessonMixin, generics.CreateAPIView):
    lookup_field = 'subchapter_id'
    
    def post(self, request, *args, **kwargs):
        #TODO: любой может добавлять подразделы, исправить
        print(self.kwargs)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(subchapter=Subchapter.objects.get(pk=self.kwargs.get(self.lookup_field)))
            return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteLesson(CourseOwnerMixin, LessonMixin, generics.DestroyAPIView):
    lookup_field = 'pk'

class RetrieveUpdateLesson(CourseOwnerMixin, LessonMixin, generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'

class AddLessonContent(CourseOwnerMixin, LessonContentMixin, generics.CreateAPIView):
    lookup_field = 'lesson_id'
    
    def post(self, request, *args, **kwargs):
        #TODO: любой может добавлять подразделы, исправить
        try:
            model = ContentType.objects.get(app_label="courses", model=kwargs.get("lesson_content_type")).model_class()
            if model is Text:
                content = request.data.get("content")
                if content:
                    instance = model.objects.create(content=content)
                    serializer = self.get_serializer(data=request.data)
                    if serializer.is_valid() and kwargs.get("lesson_content_type"):
                        serializer.save(lesson=Lesson.objects.get(pk=self.kwargs.get(self.lookup_field)),
                                        item=instance)
                        return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
                    return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif model is Code:
                content = request.data.get("content")
                language = request.data.get("language")
                if content:
                    instance = model.objects.create(content=content, language=language)
                    serializer = self.get_serializer(data=request.data)
                    if serializer.is_valid() and kwargs.get("lesson_content_type"):
                        serializer.save(lesson=Lesson.objects.get(pk=self.kwargs.get(self.lookup_field)),
                                        item=instance)
                        return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
                    return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                return response.Response({"success": False, "message": "Неверный тип контента урока"},
                                     status=status.HTTP_100_CONTINUE)
        except ContentType.DoesNotExist:
            return response.Response({"success": False, "message": "Неверный тип контента урока"},
                                     status=status.HTTP_404_NOT_FOUND)

class DeleteLessonContent(CourseOwnerMixin, LessonContentMixin, generics.DestroyAPIView):
    lookup_field = 'pk'

class RetrieveUpdateLessonContent(CourseOwnerMixin, LessonContentMixin, generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'