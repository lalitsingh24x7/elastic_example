from datetime import datetime
from elasticsearch_dsl import Document, Date, Integer, Keyword, Text, Object, Nested, Boolean, InnerDoc
from elasticsearch_dsl.connections import connections
from django.conf import settings

# Define a default Elastic search client
connections.create_connection(hosts=[settings.ELASTIC_HOST])


class Color(InnerDoc):
    id = Integer(),
    name = Text(analyzer='snowball', fields={'raw': Keyword()})


class Category(InnerDoc):
    id = Integer(),
    name = Text(analyzer='snowball', fields={'raw': Keyword()})


class Brand(InnerDoc):
    id = Integer(),
    name = Text(analyzer='snowball', fields={'raw': Keyword()})


class ProductDocument(Document):
    name = Text(analyzer='snowball', fields={'raw': Keyword()})
    slug = Keyword()
    color = Color
    category = Nested(Category)
    is_sold = Boolean()
    size = Keyword()
    price = Brand

    class Index:
        name = 'product'

