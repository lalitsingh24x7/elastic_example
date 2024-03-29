from django.contrib import admin

from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_sold', 'brand', 'price')


admin.site.register(models.Size)
admin.site.register(models.Color)
admin.site.register(models.Category)
admin.site.register(models.Brand)
