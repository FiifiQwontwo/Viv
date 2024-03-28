from django.db import models


# Create your models here.
class Project(models.Model):
    pro_title = models.CharField(max_length=100)

