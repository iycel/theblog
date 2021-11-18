from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return 'logusers/{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path, default='avatar_default.png')
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user}'
