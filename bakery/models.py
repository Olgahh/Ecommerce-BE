from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Category(models.Model):
    title= models.CharField(max_length = 200)
    image = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.title

class Product(models.Model):
    name=models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=7,decimal_places=3,default = 0)
    image = models.ImageField(null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    # GENDERS = (('M', 'Male'),('F', 'Female'))
    # gender = models.CharField(max_length=2,choices=GENDERS,default='M')
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwarg):    
    if created:
        Profile.objects.create(user=instance)