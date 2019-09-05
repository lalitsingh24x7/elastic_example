from django.core.management.base import BaseCommand

from elastic.helper import create_or_update, init_doc
from product.models import Product


class Command(BaseCommand):
    help = "Sync data from database to elastic search."

    def handle(self, *args, **options):
        init_doc()
        for product in Product.objects.all():
            create_or_update(product)

