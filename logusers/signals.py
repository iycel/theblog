# Diyorum ki, ben bir user oluşturduğumda signal gönder. Bu signali al ve profile oluştur
# sonra apps.py a git ve  
# def ready(self):
#    import logusers.signals   
# ekle
from django.db.models.signals import post_save  # önce signal i sonra signal i  alan receiver i import edeceğiz
from django.contrib.auth.models import User
from django.dispatch import receiver
from logusers.models import Profile  # user oluşturulduğunda profile otomatik oluşması için Profile i import ediyoruz

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# yada
  
# @receiver(post_save, sender=User)
# def create_profile(sender, instance, **kwargs):
#     instance.profile.save()
