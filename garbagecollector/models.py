from django.contrib.auth.models import User
from django.db import models


class Organization(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    operation_area = models.CharField(max_length=100)
    phone_one = models.CharField(max_length=12)
    phone_two = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100)
    manager_phone = models.CharField(max_length=12)
    manager_email = models.EmailField()
    checked = models.BooleanField(default=False)

    def __str__(self):
            return self.name

    class Meta:
        verbose_name_plural = "Organizations"


class Trash(models.Model): 
    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name


class UserMessage(models.Model):
    creation_date =  models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

