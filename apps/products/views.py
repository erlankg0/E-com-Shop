from django.shortcuts import render
from apps.products.models import Product


def product_detail(request, slug):
    context = {"product": Product.objects.get(slug=slug)}
    return render(request, 'products/product_detail.html', context=context)
