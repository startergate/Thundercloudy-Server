import json

import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello world")


def session(request):
    if request.method != "POST":
        return

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
    return JsonResponse({"is_succeed": True})


def download(request, file_id):
    return JsonResponse({"is_succeed": True})


def get_file_list(request):
    return JsonResponse({"is_succeed": True,
                         "files": []})
