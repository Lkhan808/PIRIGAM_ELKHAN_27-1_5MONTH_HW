from django.db import models
from django.db.models import Count


class Category(models.Model):
    name = models.CharField(max_length=20)

    @property
    def count_products(self):
        return self.products.all().count()

    def __str__(self): return self.name


class Product(models.Model):
    image = models.ImageField(null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    @property
    def filtered_reviews(self): return self.reviews.all()

    @property
    def rating(self):
        reviews = self.reviews.all().count()
        stars = sum([i.stars for i in self.reviews.all()])
        if stars and reviews:
            return stars//reviews
        else:
            pass

    def __str__(self): return self.title


STARS_CHOICE = (
    (1, '*'),
    (2, 2 * '*'),
    (3, 3 * '*'),
    (4, 4 * '*'),
    (5, 5 * '*'),
)


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(default=5, choices=STARS_CHOICE)

    def __str__(self):
        return self.text

