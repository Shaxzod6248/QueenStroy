from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Category, Product, Banner
from .serializers import CategorySerializer, ProductSerializer, BannerSerializer


class CategoryAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class ProductAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(
            products, context={'request': request}, many=True)
        return Response(serializer.data)


class BannerAPIView(APIView):
    def get(self, request):
        banners = Banner.objects.all()
        serializer = BannerSerializer(
            banners, context={'request': request}, many=True)
        return Response(serializer.data)