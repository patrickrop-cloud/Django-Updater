from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    def save_admin(self):
        self.save()

