from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
 
class profile(models.Model):
   user =  models.OneToOneField(User, on_delete=models.CASCADE)
   city = ForeignKey('City',related_name=u'ser_city',on_delete=models.CASCADE)
   phone_number = models.CharField(max_length=20)
   image = models.ImageField((""), upload_to='profile/')    

# on create a new user ---> create a new empty profile 
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class City(models.Model):
    name =  models.CharField(max_length=50)