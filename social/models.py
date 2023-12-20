from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    s_login = models.CharField(max_length=255, unique=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    image = models.ImageField(upload_to='user_profile_images/', blank=True, null=True)

class Post(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_profile.user.username}'s Post"

