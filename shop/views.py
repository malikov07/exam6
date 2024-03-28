from django.shortcuts import render
from django.views import View
from .models import Product, Category, Product_category
from reviews.models import Review

# Create your views here.


class ShopPageView(View):
    def get(self, request):
        search = request.GET.get("search") or ""
        products = Product.objects.filter(name__icontains=search)
        categories = Category.objects.all()
        featured_products = Product.objects.filter(old_price__isnull=False)
        context = {
            "products": products,
            "categories": categories,
            "featured_products": featured_products,
        }
        return render(request, "shop/shop.html", context)


class ShopDetailView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        reviews = Review.objects.all()
        context = {"product": product, "reviews": reviews}
        return render(request, "shop/product_detail.html", context)
