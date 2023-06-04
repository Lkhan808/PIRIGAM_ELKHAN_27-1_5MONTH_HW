from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from product.models import Product, Category, Review
from product.serializers import *


@api_view(['GET', 'POST'])
def product_list_create_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = ProductSerializer(products, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        data = request.data
        product = Product.objects.create(
            title=data.get('title'),
            description=data.get('description'),
            price=data.get('price'),
            category_id=data.get('category_id')
        )
        return Response(data=ProductSerializer(product, many=False).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def product_retrieve_api_view(request, **kwargs):
    product = Product.objects.get(id=kwargs['id'])
    if request.method == 'GET':
        data = ProductRetrieveSerializer(product, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        data = request.data
        product.title = data.get('title')
        product.description = data.get('description')
        product.price = data.get('price')
        product.category_id = data.get('category_id')
        product.save()
        return Response(data=ProductRetrieveSerializer(product, many=False).data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        product.delete()
        return Response(f'Deleted{product.title}')


@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        data = CategorySerializer(categories, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        data = request.data
        category = Category.objects.create(
            name=data.get('name')
        )
        return Response(data=CategorySerializer(category, many=False).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def category_retrieve_api_view(request, **kwargs):
    category = Category.objects.get(id=kwargs['id'])
    if request.method == 'GET':
        data = CategoryRetrieveSerializer(category, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        data = request.data
        category.name = data.get('name')
        category.save()
        return Response(data=CategoryRetrieveSerializer(category, many=False).data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        category.delete()
        return Response(f'Deleted{category.name}')


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        data = ReviewSerializer(review, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        data = request.data
        review = Review.objects.create(
            text=data.get('text'),
            product_id=data.get('product_id'),
            stars=data.get('stars')
        )
        return Response(data=ReviewSerializer(review, many=False).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_retrieve_api_view(request, **kwargs):
    review = Review.objects.get(id=kwargs['id'])
    if request.method == 'GET':
        data = ReviewRetrieveSerializer(review, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        data = request.data
        review.text = data.get('text')
        review.product_id = data.get('product_id')
        review.stars = data.get('stars')
        review.save()
        return Response(data=ReviewRetrieveSerializer(review, many=False).data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        review.delete()
        return Response(f'Deleted {review.text}')


@api_view(['GET'])
def products_reviews_api_view(request):
    products = Product.objects.all()
    data = ProductReviewSerializer(products, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view()
def first_view(request):
    return Response(f'Hello {request.user}!')
