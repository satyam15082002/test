from django.db import models

from django.contrib.auth.models import User
# Create your models here.
# Create your models here.
class Upload(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="upload")
    username=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics/')
 

