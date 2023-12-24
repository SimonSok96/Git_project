from django.db import models

class Categiry(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    count = models.IntegerField()
    is_published = models.BooleanField()
    
