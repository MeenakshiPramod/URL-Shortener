
from django.db import models

class URL(models.Model):
     original_url = models.URLField()
     short_url = models.CharField(max_length=15, unique=True)
     clicks = models.IntegerField(default=0)  # Click counter

     def __str__(self):
        return f'{self.original_url} -> {self.short_url}'




