from rest_framework import serializers, response
from edit_course_zone.models import Lesson
from compiler.models import CompiledCode
from django.contrib.auth.models import User

class CompilerSerializer(serializers.ModelSerializer):
    lesson = serializers.PrimaryKeyRelatedField(queryset=Lesson.objects.all(), required=False)
    language = serializers.CharField(required=False)
    user_code = serializers.CharField(required=False)
    code_execution_end = serializers.DateTimeField(required=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    
    class Meta:
        model = CompiledCode
        fields = "__all__"
    
    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)