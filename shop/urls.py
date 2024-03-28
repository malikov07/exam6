from django.urls import path
from . import views

urlpatterns = [
    path("", views.ShopPageView.as_view(), name="shop"),
    path("<int:id>/", views.ShopDetailView.as_view(), name="shop_detail"),
]
