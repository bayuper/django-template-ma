# Models
from django.db import models

class BaseModel(models.Model):
    id = models.AutoField
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)

    def soft_delete(self):
        self.isActive = False
        self.save()

    def restore(self):
        self.isActive = True 
        self.save()   

class Product(BaseModel):
    name = models.CharField(max_length=255)
    

class Category(BaseModel):
    name = models.CharField(max_length=255)
    product = models.ForeignKey    


class Subcategory(BaseModel):
    name = models.CharField(max_length=255)
    Category = models.ForeignKey      

# DRY: Dont Repeat Yourself