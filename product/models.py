from django.db import models
from django.template.defaultfilters import slugify


class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, null=True, default=None)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    is_sold = models.BooleanField(default=False)
    size = models.ManyToManyField(Size)
    price = models.IntegerField(default=0)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        super(Product, self).save()