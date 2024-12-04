from apps.example_app.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=255)