from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from distributor.models import Product
from .serializers import ProductListSerializer


@api_view(['GET'])
def product_list_view(request):
    products = Product.objects.all()
    data = ProductListSerializer(products, many=True).data
    print(data)
    return Response(data={'list': data})


@api_view(['GET'])
def product_item_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise NotFound('Товар не найден')
    data = ProductListSerializer(product).data
    return Response(data=data)
