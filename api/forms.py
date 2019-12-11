from django import forms

from api.models import UploadFileModel, Post


class UploadFileModelForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ('user', 'file')
        app_label = 'api'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('user', 'title', 'content')
        app_label = 'api'

