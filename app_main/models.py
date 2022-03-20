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