from rest_framework import authentication
from edit_course_zone.models import Course
from api.serializers.course_serializers import *
from api.permissions import IsOwnerOrReadOnlyCourse

class AuthorizedMixin:
    authentication_classes = (authentication.TokenAuthentication,)

class CourseOwnerMixin(AuthorizedMixin):
    permission_classes = (IsOwnerOrReadOnlyCourse,)

class CourseMixin(AuthorizedMixin):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class ChapterMixin(AuthorizedMixin):
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()

class SubchapterMixin(AuthorizedMixin):
    serializer_class = SubchapterSerializer
    queryset = Subchapter.objects.all()

class LessonMixin(AuthorizedMixin):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonContentMixin(AuthorizedMixin):
    serializer_class = LessonContentSerializer
    queryset = LessonContent.objects.all()