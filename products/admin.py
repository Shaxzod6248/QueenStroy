from django.contrib import admin
from .models import Product
from .models import Banner
from .models import Category


admin.site.register(Product)
admin.site.register(Banner)
admin.site.register(Category)