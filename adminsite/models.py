from django.db import models


class User(models.Model):

    name = models.CharField(max_length=25)
    tel = models.CharField(max_length=20)
    language = models.CharField(max_length=20)


class Order(models.Model):
    user_fk_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_order")
