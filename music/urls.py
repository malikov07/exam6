from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import AlbomsAPIViewSet,ArtistsAPIViewSet,SongsAPIViewSet,HomeApiView
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(prefix="songs", viewset=SongsAPIViewSet, basename="songs")
router.register(prefix="alboms", viewset=AlbomsAPIViewSet, basename="alboms")
router.register(prefix="artists", viewset=ArtistsAPIViewSet, basename="artists")


urlpatterns = [
    path("",HomeApiView.as_view(), name="home"),
    path("", include(router.urls)),
    path("auth/gen-token/", views.obtain_auth_token),
]