from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from product.models import Product, Category, Review
from product.serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination


# @api_view(['GET', 'PUT', 'DELETE'])
# def product_retrieve_api_view(request, **kwargs):
#     product = Product.objects.get(id=kwargs['id'])
#     if request.method == 'GET':
#         data = ProductRetrieveSerializer(product, many=False).data
#         return Response(data=data, status=status.HTTP_200_OK)
#     if request.method == 'PUT':
#         data = request.data
#         product.title = data.get('title')
#         product.description = data.get('description')
#         product.price = data.get('price')
#         product.category_id = data.get('category_id')
#         product.save()
#         return Response(data=ProductRetrieveSerializer(product, many=False).data, status=status.HTTP_200_OK)
#     if request.method == 'DELETE':
#         product.delete()
#         return Response(f'Deleted{product.title}')


class CategoryModelView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination


# @api_view(['GET', 'PUT', 'DELETE'])
# def category_retrieve_api_view(request, **kwargs):
#     category = Category.objects.get(id=kwargs['id'])
#     if request.method == 'GET':
#         data = CategoryRetrieveSerializer(category, many=False).data
#         return Response(data=data, status=status.HTTP_200_OK)
#     if request.method == 'PUT':
#         data = request.data
#         category.name = data.get('name')
#         category.save()
#         return Response(data=CategoryRetrieveSerializer(category, many=False).data, status=status.HTTP_200_OK)
#     if request.method == 'DELETE':
#         category.delete()
#         return Response(f'Deleted{category.name}')


class ReviewModelView(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination


# @api_view(['GET', 'PUT', 'DELETE'])
# def review_retrieve_api_view(request, **kwargs):
#     review = Review.objects.get(id=kwargs['id'])
#     if request.method == 'GET':
#         data = ReviewRetrieveSerializer(review, many=False).data
#         return Response(data=data, status=status.HTTP_200_OK)
#     if request.method == 'PUT':
#         data = request.data
#         review.text = data.get('text')
#         review.product_id = data.get('product_id')
#         review.stars = data.get('stars')
#         review.save()
#         return Response(data=ReviewRetrieveSerializer(review, many=False).data, status=status.HTTP_200_OK)
#     if request.method == 'DELETE':
#         review.delete()
#         return Response(f'Deleted {review.text}')


class ReviewProductAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReviewSerializer

