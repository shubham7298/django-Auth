from django.db import models

class UserInfo(models.Model):
    id = models.AutoField( auto_created = True, primary_key = True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=1000)

