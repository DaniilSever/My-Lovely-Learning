from rest_framework import permissions
from courses.models import Course
from api.views.course_views import *

class IsOwnerOrReadOnlyCourse(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        name_of_class = view.__class__.__name__
        if "Course" in name_of_class:
            pass
        elif "Chapter" in name_of_class:
            obj = obj.course
        elif "Subchapter" in name_of_class:
            obj = obj.chapter.course
        elif "LessonContent" in name_of_class:
            obj = obj.lesson.subchapter.chapter.course
        elif "Lesson" in name_of_class:
            obj = obj.subchapter.chapter.course
        
        if request.method in permissions.SAFE_METHODS and \
            obj.visibility == Course.VisibilityChoice.PUBLIC:
            return True
        
        return request.user in obj.owners.all() or request.user.is_staff