from django.shortcuts import render
from django.http import HttpResponse

from store import models as store_models


# Create your views here.

def index(request):
    products = store_models.Product.objects.filter(status="Published")
    context = {
        "products": products 
    }
    return render(request, "store/index.html", context)

def product_detail(request, slug):
    product = store_models.Product.objects.get(status="Published", slug=slug)
    related_product = store_models.Product.objects.filter(category=product.category, status="Published").exclude(id=product.id)
    product_stock_range = range(1, product.stock + 1)

    context = {
        "product": product,
        "related_product": related_product,
        "product_stock_range": product_stock_range, 
    }
    return render(request, "store/product_detail.html", context)