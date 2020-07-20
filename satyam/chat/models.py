from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Group(models.Model):
    group_name=models.CharField(max_length=100)
    memeber=models.ManyToManyField(User,blank=True,related_name="group")
    admin=models.CharField(max_length=100)
    def __str__(self):
        return self.group_name

class Message(models.Model):
    name=models.CharField(max_length=100)
    msg=models.TextField()
    grp=models.ForeignKey(Group,on_delete=models.CASCADE,related_name="message")

    def __str__(self):
        return self.name