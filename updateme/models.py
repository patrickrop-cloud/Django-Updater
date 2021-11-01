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

    def __str__(self):
        return self.name

    def create_neighbourhood(self):
        pass
    
    def update_neighbourhood(self):
        pass

    def delete_neighbourhood(self):
        self.delete() 

class User(models.Model):
    name=models.CharField(max_length=50, null=True)
    id = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=30,null=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=CASCADE, null=True)



    def __str__(self):
        return self.name


    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()

class Business(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=CASCADE, null=True)
    email = models.EmailField(max_length=30, null=True)

    def __str__(self):
        return self.name

    def create_business(self):
        pass

    def update_business(self):
        pass

    def search_business(self):
        pass

    def delete_business(self):
        self.delete()
    


