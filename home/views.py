from django.shortcuts import render
from django.views import View
from shop.models import Product,Category
from reviews.models import Testimonial
# Create your views here.

class HomePageView(View):
    def get(self,request):
        search = request.GET.get("search") or ''
        products = Product.objects.filter(name__icontains = search)
        bestsellers = Product.objects.filter(rating__gt=4)
        categories = Category.objects.all()
        testimonials = Testimonial.objects.all()
        context = {
            "products": products,
            "categories": categories,
            "bestsellers": bestsellers,
            "testimonials": testimonials,
        }
        return render(request, "home/home.html",context)
