from django.db import models


class review(models.Model):
    email = models.EmailField(max_length=256, default='')
    message = models.CharField(max_length=256, default='')
    name = models.CharField(max_length=256, default='')
    ratings = models.CharField(max_length=256, default='')


class indiansav_contact(models.Model):
    name = models.CharField(max_length=256, default='')
    message = models.CharField(max_length=256, default='')
    email = models.EmailField(max_length=256, default='')
    phone = models.CharField(max_length=20, default='')



# Create your models here.
