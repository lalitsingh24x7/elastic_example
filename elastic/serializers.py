from rest_framework import serializers
from product.models import Product, Size,  Color, Brand, Category


"""
    name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    is_sold = models.BooleanField(default=False)
    size = models.ManyToManyField(Size)
    price = models.IntegerField(default=0)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
"""


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'name')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    category = CategorySerializer(many=True)
    size = serializers.SerializerMethodField()
    brand = BrandSerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'color', 'category', 'is_sold', 'size', 'price', 'brand')

    def get_size(self, obj):
        return list(obj.size.values_list('name', flat=True))
