import json
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from api.models import UploadFileModel
from .forms import UploadFileModelForm

# Create your views here.


def index(request):
    return HttpResponse("Hello world")


def session(request):
    if request.method != "POST":
        return HttpResponse(status=500)

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    res = requests.post('http://sid.donote.co:3000/api/v1/session/', {
        "type": "login",
        "clientid": body["clientid"],
        "userid": body["id"],
        "password": body["pw"],
        "isPermanent": True,
    }).json()
    if res["type"] == "error":
        return HttpResponse(status=500)
    return JsonResponse({
        "sessid": res["response_data"][0],
        "pid": res["response_data"][1],
        "nickname": res["response_data"][2],
        "expire": res["response_data"][3],
    })


def upload(request):
    file = UploadFileModel(title="something random")
    form = UploadFileModelForm(request.POST, request.FILES, instance=file)
    if form.is_valid():
        form.save()
        return JsonResponse({"is_succeed": True})
    else:
        return HttpResponse(status=500)


def download(request, file_id):
    return JsonResponse({"is_succeed": True})


def get_file_list(request):

    return JsonResponse({"is_succeed": True,
                         "files": []})
