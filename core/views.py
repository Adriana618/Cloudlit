import subprocess
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def execute(request):
    data = request.data
    code = data.get("code","")
    filename = data.get("filename","")
    extension = data.get("extension","")
    FILE = "{}.{}".format(filename,extension)
    with open(FILE,"+w") as File:
        File.write(code)
    
    execution = subprocess.Popen(["python3",FILE],
                                    stdin = subprocess.PIPE,
                                    stdout = subprocess.PIPE,
                                    stderr = subprocess.PIPE,
                                    universal_newlines = True,
                                    bufsize=0)
    while execution.poll() == None:
        pass
    if execution.poll() == 1:
        return Response({"output":execution.stderr.readlines()}, status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        return Response({"output":execution.stdout.readlines()}, status=status.HTTP_200_OK)