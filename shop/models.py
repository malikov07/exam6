from django.db import models
from users.models import User


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=90)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(60)
    product_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class QuantityRole(models.TextChoices):
    kilo = ("kg", "kilogram") 
    liter = ("l" ,"liter")
    piece = ("p","piece")


class Product(models.Model):
    name = models.CharField(max_length=90)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="shop/product_image/")
    old_price = models.FloatField(null=True)
    new_price = models.FloatField()
    quantity = models.CharField(
        max_length=10, choices=QuantityRole, default=QuantityRole.kilo
    )
    rating = models.FloatField()
    origin_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + self.description[:10]


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name


class Product_category(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.product.name +" "+ self.category.name
