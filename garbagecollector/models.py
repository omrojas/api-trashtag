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
    icon_url = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name


class UserMessage(models.Model):
    creation_date =  models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject


class Level(models.Model):
    name = models.CharField(max_length=100)
    cleanups = models.IntegerField()
    
    def __str__(self):
        return self.name


class UserProfile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True,)

    def __str__(self):
        return self.user.username


class Cleanup(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=20, null=True)
    longitude = models.CharField(max_length=20, null=True)

    def __str__(self):
        return '{}'.format(self.id)


class TrashCleanup(models.Model):
    cleanup = models.ForeignKey(Cleanup, on_delete=models.CASCADE)
    trash = models.ForeignKey(Trash, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    

    def __str__(self):
        return self.trash.name


class UserOrganization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username