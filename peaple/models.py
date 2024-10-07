from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class People(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null= True, blank= True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField(null=True)

    def __str__(self):
        return self.name