from rest_framework import generics, views, response
from api.serializers.user_serializers import *
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import authentication, permissions, authtoken
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginUser(views.APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                username, email = serializer.validated_data.get('username'), serializer.validated_data.get('email')
                if username:
                    user = User.objects.get(username=username)
                elif email:
                    user = User.objects.get(email=email)
            except ObjectDoesNotExist:
                return response.Response({"success": False, "message": "user does not exist"})
                
            if check_password(serializer.validated_data['password'], user.password):
                token = authtoken.models.Token.objects.get_or_create(user=user)
                return response.Response({"success": True, "token": token[0].key})
            else:
                return response.Response({"success": False, "message": "incorrect password"})

class RetrieveUser(generics.RetrieveAPIView):
    queryset = User.objects.all().values()
    serializer_class = UserSerializer

class UpdateUser(views.APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def put(self, request):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return response.Response({"success": True, "message": "user updated"})
        else:
            return response.Response({"success": False, "message": f"error updating user.\nErrors: {serializer.errors}"})

class DeleteUser(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def destroy(self, request):
        user = User.objects.get(id=request.user.id)
        self.perform_destroy(user)
        return response.Response({"success": True, "message": "user deleted"})