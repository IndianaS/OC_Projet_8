from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product, Favorite
from sentry_sdk import capture_message


def result_search(request):
    """Django view search result page."""

    result = None
    try:
        product_search = request.GET['q']
        capture_message(
            f"Recherche de l'utilisateur : {product_search}", level="info")
        product = Product.objects.filter(
            product_name_fr__icontains=product_search).first()
        if product:
            substituts = product.better_products()
        else:
            product = None
            substituts = None

    except KeyError:
        print('Pas de requête')

    return render(
        request,
        'products/result_search.html',
        {'substituts': substituts, 'product': product}
    )


def product_sheet(request, code):
    """Django view product page."""

    product = get_object_or_404(Product, id=code)
    return render(request, 'products/product_sheet.html', {'product': product})


def favorites(request):
    """Django view favorite recording page."""

    if request.method == 'POST':
        user = request.user
        id_substitut = request.POST['id_substitut']
        id_product = request.POST['id_product']

        substitut = Product.objects.get(id=id_substitut)
        product = Product.objects.get(id=id_product)
        product_save = Favorite.objects.get_or_create(
            user=user,
            product=product,
            substitute=substitut
        )
        return redirect('products:product_sheet', code=id_substitut)

    return redirect('home')
