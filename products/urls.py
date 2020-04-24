from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("", views.result_search, name="result_search"),
    path("details/<int:code>/", views.product_sheet, name="product_sheet"),
    path("favorites", views.favorites, name="favorites"),
]
