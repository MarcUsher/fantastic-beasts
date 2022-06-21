from django.db import models

# Create your models here.
class Beast(models.Model):
    name = models.CharField(max_length=100)
    native = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    size = models.CharField(max_length=100)
    danger = models.PositiveSmallIntegerField()
    image = models.URLField(max_length=500)