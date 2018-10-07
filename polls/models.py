from django.db import models

# Create your models here.
class VideoInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"视频名")
    path = models.EmailField()
