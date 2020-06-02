from django.shortcuts import render
from django.http import JsonResponse

from products.models import Product


def complete(request):
    searched_term = request.GET.get("term")
    product = Product.objects.get_all_by_term(searched_term)
    product = [product.name for product in product]
    return JsonResponse(product, safe=False)
