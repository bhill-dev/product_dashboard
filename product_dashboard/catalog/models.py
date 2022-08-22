from django.db import models
from django.urls import reverse
import uuid


class Category(models.Model):
    name = models.CharField(max_length=200)
    help_text = 'Enter a product category (e.g. phone)'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)
    help_text = 'Enter a product Tag (e.g. Camera)'

    def __str__(self):
        return self.name


class Product(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)

    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag, help_text='Enter a tag for this product')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this product')

    def __str__(self):
        return f"{self.make} {self.model}"

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])
