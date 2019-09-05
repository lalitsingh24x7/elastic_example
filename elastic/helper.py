from django.conf import settings
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

from elastic import documents
from elastic import serializers

ES_HOST = {"host": settings.ELASTIC_HOST}
client = Elasticsearch(hosts=[ES_HOST])


def init_doc():
    documents.ProductDocument.init()


def create_or_update(product):
    data = serializers.ProductSerializer(product).data
    doc = documents.ProductDocument(meta={"id": product.id}, **data)
    doc.save(refresh=True)


def get_product(query, limit, offset):
    query = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["brand.name^5", "name"]
            }
        },
        "size": limit,
        "from": offset
    }
    search = Search(index='product', using=client)
    search = search.from_dict(query)
    response = search.execute()
    total = response['hits']['total']
    data = [item['_source'].to_dict() for item in response['hits']['hits']]
    return total, data
