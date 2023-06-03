from django.urls import path
from api.views.compiler_views import *

app_name = "compiler_api"

urlpatterns = [
    path('', CompileCodeView.as_view(), name="compile")
]
