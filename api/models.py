from django.db import models

# Create your models here.


class UploadFileModel(models.Model):

    def __str__(self):
        return self.title
    user = models.CharField(max_length=64)
    file = models.ImageField(blank=False, null=True)