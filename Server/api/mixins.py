from courses.models import Course
from api.serializers.course_serializers import *
from api.permissions import IsOwnerOrReadOnlyCourse

class CourseOwnerMixin:
    permission_classes = (IsOwnerOrReadOnlyCourse,)

class CourseMixin:
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class ChapterMixin:
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()

class SubchapterMixin:
    serializer_class = SubchapterSerializer
    queryset = Subchapter.objects.all()

class LessonMixin:
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonContentMixin:
    serializer_class = LessonContentSerializer
    queryset = LessonContent.objects.all()