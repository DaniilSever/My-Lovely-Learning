from rest_framework import generics, response, authentication, permissions, mixins
from courses.models import Course
from api.serializers.course_serializers import *
from api.mixins import *
from rest_framework import status
from django.contrib.contenttypes.models import ContentType
from courses.models import *
from django.db import IntegrityError
from api.constants import AVAILABLE_LESSON_CONTENT_MODELS



class CreateCourse(CourseMixin, generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

class DeleteCourse(CourseOwnerMixin, CourseMixin, generics.DestroyAPIView):
    lookup_field = 'pk'

class RetrieveUpdateCourse(CourseOwnerMixin, CourseMixin, generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'

class ListCourse(CourseOwnerMixin, CourseMixin, generics.ListAPIView):
    serializer_class = CourseListSerializer
    queryset = Course.objects.filter(visibility=Course.VisibilityChoice.PUBLIC)

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
        if "pk" in request.data:
            del request.data['pk']
        if "id" in request.data:
            del request.data['id']
        try:
            model = ContentType.objects.get(app_label="courses", model=kwargs.get("lesson_content_type")).model_class()
            if model in AVAILABLE_LESSON_CONTENT_MODELS:
                create_model_instance_kwargs = { field.name : request.data.get(field.name) for field in model._meta.fields }
                if model is Video:
                    create_model_instance_kwargs['url'] = create_model_instance_kwargs['url'].replace("watch?v=", "embed/")
                    print(create_model_instance_kwargs)
                try:
                    instance = model.objects.create(**create_model_instance_kwargs)
                except IntegrityError as ir:
                    return response.Response({"success": False, "error": str(ir)},
                                         status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
                content_type = ContentType.objects.get_for_model(instance)
            else:
                return response.Response({"success": False, "message": "Неверный тип контента урока"},
                                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            serializer_context = self.get_serializer_context()
            serializer_context['model_instanse'] = instance
            
            serializer = self.get_serializer(data={
                            "lesson": Lesson.objects.get(pk=self.kwargs.get(self.lookup_field)).pk,
                            'content_type': content_type.pk,
                            'object_id': instance.pk
                        }, context=serializer_context)
            
            if serializer.is_valid():
                serializer.save()
                return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except ContentType.DoesNotExist:
            return response.Response({"success": False, "message": "Неверный тип контента урока"},
                                     status=status.HTTP_404_NOT_FOUND)

class DeleteLessonContent(CourseOwnerMixin, LessonContentMixin, generics.DestroyAPIView):
    lookup_field = 'pk'

class RetrieveUpdateLessonContent(CourseOwnerMixin, LessonContentMixin, generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'

class ViewLessonContent(CourseOwnerMixin, LessonContentMixin, generics.ListAPIView):
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs):
        
        return super().get(request, *args, **kwargs)

class JoinCourse(generics.CreateAPIView):
    #TODO: если пользователь уже записался на курс, повторно он не может записаться
    queryset = CourseParticipant
    lookup_field = 'course_pk'
    serializer_class = CourseParticipantSerializer
    
    def get_serializer(self, *args, **kwargs):
        serializer = super().get_serializer(*args, **kwargs)
        serializer.initial_data["course"] = self.kwargs.get(self.lookup_field)
        serializer.initial_data["participant"] = self.request.user.id
        return serializer