from django.db import models
from rest_framework import permissions
from django.core.exceptions import ValidationError
import os


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Category(models.Model):
    name_uz = models.CharField(max_length=250)
    name_ru = models.CharField(max_length=250)

    def __str__(self):
        return self.name_ru


class Product(models.Model):
    image = models.ImageField(upload_to='products_image')
    title_uz = models.CharField(max_length=250)
    title_ru = models.CharField(max_length=250)
    description_uz = models.CharField(max_length=250)
    description_ru = models.CharField(max_length=250)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title_ru


class Banner(models.Model):
    image = models.ImageField(upload_to='banners_image')

    def __str__(self):
        return 'pic'