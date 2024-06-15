from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50)
    slug=models.CharField(max_length=50)
    parent_id=models.IntegerField()

class Posts(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    