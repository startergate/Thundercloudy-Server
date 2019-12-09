from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('/session', views.session, name="login"),
    path('/files', views.get_file_list, name="file_list"),
    path('/file', views.upload, name="upload"),
    path('/file/<str:file_id>', views.download, name="upload"),
]