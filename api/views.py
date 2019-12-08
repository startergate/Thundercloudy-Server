from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello world")


def upload(request):
    return JsonResponse({"is_succeed": True})


def download(request, file_id):
    return JsonResponse({"is_succeed": True})


def get_file_list(request):
    return JsonResponse({"is_succeed": True,
                         "files": []})
