from django import forms

from api.models import UploadFileModel


class UploadFileModelForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ('title', 'file')
        app_label = 'api'
