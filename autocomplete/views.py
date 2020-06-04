from django.shortcuts import render
from django.http import JsonResponse

from products.models import Product


def complete(request):
    searched_term = request.GET.get("term")
    product = Product.objects.filter(product_name_fr__icontains=searched_term)
    product = [product.product_name_fr for product in product]
    return JsonResponse(product, safe=False)
