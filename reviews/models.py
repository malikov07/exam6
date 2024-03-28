from django.db import models
from shop.models import Product
from users.models import User


# Create your models here.
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rate = models.FloatField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Testimonial(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to="testimonials/")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length = 60)
