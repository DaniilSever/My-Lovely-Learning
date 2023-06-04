from courses.models import *
from rest_framework import response, status

AVAILABLE_LESSON_CONTENT_MODELS = (Text, Code, Image, Video, WriteAProgram)
FORBIDDEN_RESPONSE = response.Response({"message": "Отказано в доступе"}, status=status.HTTP_403_FORBIDDEN)