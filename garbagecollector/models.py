from django.db import models


class Trash(models.Model): 
    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    