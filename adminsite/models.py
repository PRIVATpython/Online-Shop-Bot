from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    tel = models.CharField(max_length=20)

    tel = models.CharField(max_length=20)
