from django.db import models


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


class Product(models.Model):
    name = models.CharField(max_length=250)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    is_sold = models.BooleanField(default=False)
    # TODO: size should be list
    #size =
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name