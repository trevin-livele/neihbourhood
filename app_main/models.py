from django.db import models
from accounts.models import Account
from category.models import Category
# Create your models here.
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=20 ,unique=True, null=True)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(Account, on_delete=models.CASCADE,blank=True,null=True)
    date_posted  =  models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.description



# location model
class Location(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # save location
    def save_location(self):
        self.save()

    def __str__(self):
        return self.name




# NeighbourHood Model
class NeighbourHood(models.Model):
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    occupants_count = models.IntegerField(default=0)
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name





# business class model
class Business(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE,blank=True,null=True)
    description = models.CharField(max_length=200,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bs_description


# contact class model
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50)
    user = models.ForeignKey(Account, on_delete=models.CASCADE,blank=True,null=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
