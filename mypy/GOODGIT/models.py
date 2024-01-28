from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Categiry(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    count = models.IntegerField()
    is_published = models.BooleanField()
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
    # date_create = models.DateTimeField(User, auto_now=True)
    def __str__(self):
        return self.user.username
    
def create_profle(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()
post_save.connect(create_profle, sender=User)
    