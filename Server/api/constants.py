from edit_course_zone.models import *
from rest_framework import response, status

AVAILABLE_LESSON_CONTENT_MODELS = (Text, Code, Image, Video)
FORBIDDEN_RESPONSE = response.Response({"message": "Отказано в доступе"}, status=status.HTTP_403_FORBIDDEN)