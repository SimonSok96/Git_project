from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Tweet

admin.site.unregister(Group)
admin.site.unregister(User)


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]
    
# @admin.register(TweetLikes)
# class BloglikesAdmin(admin.ModelAdmin):
#     autocomplete_fields = ['likes_by', 'tweet_post']
#     list_display = ('tweet_post', 'liked_by', 'like', 'created')
    
admin.site.register(Tweet)
    
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)