from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify  # adresde yazan slug ifadelerinin arasına - koyar
from .models import Post

@receiver(pre_save, sender=Post)
def pre_save_create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + ' ' + instance.title)