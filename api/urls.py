from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('/files', views.get_file_list, name="file_list"),
    path('/file', views.upload, name="upload"),
    path('/file/<string:file_id>', views.download, name="upload"),
]