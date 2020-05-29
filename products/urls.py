from django.urls import path

from . import views

app_name = "products"

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path("", views.result_search, name="result_search"),
    path("details/<int:code>/", views.product_sheet, name="product_sheet"),
    path("favorites", views.favorites, name="favorites"),
    path('sentry-debug/', trigger_error),
]
