from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Expense(models.Model):
    name=models.CharField(max_length=256)
    cost = models.FloatField()    
    date = models.DateField(default=now)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.CharField(max_length=266)

    def __str__(self):
        return self.status

    class Meta:
        ordering: ('-date')


class Status(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'status'

    def __str__(self):
        return self.name