from django.db import models
from django.utils import timezone

class Music(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    upload_date = models.DateTimeField(default=timezone.now)
    song = models.FileField(upload_to='')

    def __str__(self):
        return self.title