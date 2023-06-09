from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import CategoryAPIView, ProductAPIView, BannerAPIView, ProductDetail, CategoriesDetail


urlpatterns = [
    path('categories/', CategoryAPIView.as_view()),
    path('products/', ProductAPIView.as_view()),
    path('banners/', BannerAPIView.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('categories/<int:pk>/', CategoriesDetail.as_view()),
]