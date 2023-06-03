from rest_framework import generics, views, response, authentication, permissions
from courses.models import Course
from api.serializers.course_serializers import *
from api.mixins import CourseOwnerMixin

class CreateCourse(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)

class DeleteCourse(CourseOwnerMixin, generics.DestroyAPIView):
    lookup_field = 'pk'
    
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        pk = kwargs.get("pk")
        return response.Response({"success": True, "message": f"Курс с id {pk} был успешно удалён"})

class RetrieveCorse(CourseOwnerMixin, generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'
    
    def put(self, request):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return response.Response({"success": True, "message": "Курс был успешно обновлён"})
        else:
            return response.Response({"success": False, "message": f"Возникла ошибка при обновлении.\nErrors: {serializer.errors}"})