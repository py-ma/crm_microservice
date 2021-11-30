from django.db import models

class ModelsForm(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)



