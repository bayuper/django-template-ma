from django.db import models

class BaseModel(models.Model):
    id = models.AutoField
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)