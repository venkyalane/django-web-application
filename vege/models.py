from django.db import models

# Create your models here.
class recipi(models.Model):
    recipi_name = models.CharField(max_length=100)
    recipi_desc = models.CharField(max_length=500)
    recipi_img = models.ImageField(upload_to='SampleProject/vege/receipe')


    def __str__(self):
        return self.recipi_name