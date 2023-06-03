from rest_framework import generics, views, response, authentication, permissions
from edit_course_zone.models import Course, Code
from compiler.models import CompiledCode
from api.serializers.compiler_serializers import CompilerSerializer
from api.serializers.course_serializers import *
import subprocess, os, sys, json
from django.conf import settings
from datetime import datetime
from api.utils import save_serializer

compiler_dir = settings.COMPILER_ROOT

class CompileCodeView(generics.CreateAPIView):
    queryset = CompiledCode.objects.all()
    serializer_class = CompilerSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        if request.data.get("language") in Code.LanguageChoice.labels and request.data.get('user_input', None):
            language = request.data.get("language")
            user_input = request.data.get('user_input')
            p = os.path.join(compiler_dir, language, str(request.user.id))
            os.makedirs(p, 0o777, exist_ok=True)
            match language:
                case "python":
                    with open(f'{p}/main.py', 'w') as f:
                        f.write(user_input)
                    start_time = datetime.now()
                    comp_p = subprocess.Popen(f"docker run -it --rm -v {p}:/compiler python/3.10 sh -c 'python3 /compiler/main.py'", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                case _:
                    print('Неизвестный язык')
            
            comp_p.wait(timeout=10)
            res = comp_p.stdout.read().decode("utf-8")
            
            end_time = datetime.now()
            
            serializer = self.get_serializer(data={
                "user": request.user.id,
                #TODO: lesson
                "language":language,
                "user_code": user_input,
                "code_execution_start": start_time,
                "code_execution_end": end_time
            })
            
            if comp_p.returncode:
                serializer.initial_data.update({"errors": res})
                save_serializer(serializer)
                return response.Response({"success": True, "errors": res})
            serializer.initial_data.update({"result": res})
            save_serializer(serializer)
            return response.Response({"success": True, "result": res})
        return response.Response({"success": False, "message": "Неизвестный язык программирования"})