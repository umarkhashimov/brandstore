from django.db import models

# Create your models here.


class SizesModel(models.Model):
    size_name = models.CharField(max_length=5)

    def __str__(self):
        return self.size_name
    

class ColorsModel(models.Model):
    color_name = models.CharField(max_length=50)

    def __str__(self):
        return self.color_name

class TagsModel(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name


class ProdutsModel(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='products/')
    description = models.TextField(max_length=500)
    price = models.PositiveIntegerField()
    tags = models.ManyToManyField(TagsModel)
    colors = models.ManyToManyField(ColorsModel)
    sizes = models.ManyToManyField(SizesModel)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

