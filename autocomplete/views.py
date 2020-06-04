from django.shortcuts import render
from django.http import JsonResponse

from products.models import Product


def complete(request):
    searched_term = request.GET.get("term")
    products = Product.objects.filter(product_name_fr__icontains=searched_term)
    autocomplete_products = [products.product_name_fr for products in products][:10]
    return JsonResponse(autocomplete_products, safe=False)
