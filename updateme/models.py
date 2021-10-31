from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    def save_admin(self):
        self.save()

    def delete_admin(self):
        self.delete()

class NeighbourHood(models.Model):
    name = models.CharField(max_length=30,null=False)
    location = models.CharField(max_length=30, null=False)
    admin = models.ForeignKey(Admin, on_delete=CASCADE, null=True)
    occupants_count = models.IntegerField(default=0, null=False)

