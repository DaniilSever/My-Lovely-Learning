from django.urls import path
from api.views.user_views import *

app_name = "user_api"

urlpatterns = [
    path('create/', CreateUser.as_view(), name="create"),
    path('login/', LoginUser.as_view(), name="login"),
    path('<int:pk>/', RetrieveUser.as_view(), name="retrieve"),
    path('update/', UpdateUser.as_view(), name="update"),
    path('delete/', DeleteUser.as_view(), name="delete")
    # TODO: get course participants
    # TODO: get statistics
    # TODO: reset password and mail
]
