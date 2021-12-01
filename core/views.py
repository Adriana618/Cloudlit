import os
import subprocess
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def execute(request):
    data = request.data
    code = data.get("code", "")
    filename = data.get("filename", "")
    extension = data.get("extension", "")
    if not os.path.exists("temp"):
        os.makedirs("temp")
    FILE = "temp/{}.{}".format(filename, extension)
    with open(FILE, "+w") as File:
        File.write(code)
    execution = subprocess.Popen(
        ["python3", FILE],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        bufsize=0,
    )

    while execution.poll() is None:
        pass
    if execution.poll() == 1:
        response = {"output": execution.stderr.readlines()}
        os.remove(FILE)
        return Response(
            response,
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
    else:
        response = {"output": execution.stdout.readlines()}
        os.remove(FILE)
        return Response(
            response,
            status=status.HTTP_200_OK
        )


def login(request):
    return render(request, "editor.html")
