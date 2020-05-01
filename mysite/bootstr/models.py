from django.db import models
from .validators import validate_file_extension
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=30)
    featured_image = models.FileField(upload_to="static/images/%Y/%m/%d", validators=[validate_file_extension])
    body = models.CharField(max_length=1000)

    def __str__(self):
        return self.title