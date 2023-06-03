from rest_framework import generics, views, response, authentication, permissions
from edit_course_zone.models import Course, Code
from compiler.models import CompiledCode
from api.serializers.compiler_serializers import CompilerSerializer
from api.serializers.course_serializers import *
import subprocess, os, sys, json
from django.conf import settings

compiler_dir = settings.COMPILER_ROOT

class CompileCodeView(generics.CreateAPIView):
    queryset = CompiledCode.objects.all()
    serializer_class = CompilerSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        if request.data.get("lang") in Code.LanguageChoice.labels and request.data.get('user_input', None):
            language = request.data.get("lang")
            p = os.path.join(compiler_dir, language, str(request.user.id))
            os.makedirs(p, 0o777, exist_ok=True)
            match language:
                case "python":
                    with open(f'{p}/main.py', 'w') as f:
                        f.write(request.data.get('user_input'))
                    
                    comp = subprocess.Popen(f"docker run -it --rm -v {p}:/compiler python/3.10 sh -c 'python3 /compiler/main.py'", stdout=subprocess.PIPE, shell=True)
                    res = comp.stdout.read().decode("utf-8")
                case _:
                    print('Неизвестный язык')
            
            # return super().post(request, *args, **kwargs)
            return response.Response({"success": True, "message": res})
        return response.Response({"success": False, "message": "Неизвестный язык программирования"})