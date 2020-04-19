from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
def __str__(self):
  return self.user.username

class Docter(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False, auto_now_add=False)
    mobile=models.CharField(max_length=20)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)