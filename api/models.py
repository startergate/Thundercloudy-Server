from django.db import models

# Create your models here.


class UploadFileModel(models.Model):
    class Meta:
        # app_label = 'uploadFileModel'
        pass
    def __str__(self):
        return self.title
    title = models.CharField(max_length=50)
    file = models.ImageField(blank=False, null=True)