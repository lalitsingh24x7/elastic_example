from rest_framework import views
from rest_framework.response import Response
from elastic.helper import get_product


class ProductView(views.APIView):
    def get(self, request, format=None):
        """
        Return a list of all product from elastic search.
        """
        limit = request.GET.get('limit', 10)
        offset = request.GET.get('offset', 0)
        query = request.GET.get('query', '')
        total, data = get_product(query, limit, offset)
        result = dict(
            data=data,
            count=total,
            limit=limit,
            offset=offset
        )
        return Response(result)