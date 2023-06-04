from rest_framework import serializers

from product.models import *


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars product_id'.split()


class ProductReviewSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_reviews(self, product):
        return [i.stars for i in product.reviews.all()]

    def get_rating(self, product):
        return product.rating


class ReviewRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    count_products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_count_products(self, category):
        return category.count_products


class CategoryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    filtered_reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ('image', 'title', 'description', 'price', 'category', 'filtered_reviews')


class ProductRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
