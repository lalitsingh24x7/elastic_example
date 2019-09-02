from . import documents
from . import serializers


def init_doc():
    documents.ProductDocument.init()


def save_from_db_to_els(product):
    data = serializers.ProductSerializer(product).data
    doc = documents.ProductDocument(meta={"id": product.id}, **data)
    doc.save(refres=True)