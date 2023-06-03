from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import authtoken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    
    def create(self, validated_data):
        raw_password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(raw_password=raw_password)
        user.save()
        authtoken.models.Token.objects.get_or_create(user=user)
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField()