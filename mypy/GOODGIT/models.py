from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings

class Categiry(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    count = models.IntegerField()
    is_published = models.BooleanField()
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
    date_create = models.DateTimeField(User, auto_now=True)
    def __str__(self):
        return self.user.username
    
def create_profle(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()
post_save.connect(create_profle, sender=User)


class Tweet(models.Model):
    user = models.ForeignKey(User, related_name="tweets", on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="tweet_like", blank=True)
    
    def likesnum(self):
        return self.likes.count()
    
    def __str__(self):
        return f"{self.user} ({self.created_at:%Y-%m-%d %H:%M}): {self.body}"
    
    
# class TweetLikes(models.Model):
#     tweet_post = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Твитт в блоге')
#     liked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
#     like = models.BooleanField('Like', default=False)
#     created = models.DateTimeField('Дата и время', auto_now_add=True)
    

#     class Meta:
#         verbose_name = 'Blog Like'
#         verbose_name_plural = 'Blog likes'

#     def __str__(self):
#         return f'{self.liked_by}: {self.tweet_post} {self.like}'

    