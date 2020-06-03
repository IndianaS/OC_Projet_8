from django.test import TestCase
from django.urls import resolve
from django.shortcuts import reverse

from products.views import result_search, product_sheet, favorites, delete_favorites


class UrlTestCase(TestCase):

    def test_result_search_url_view(self):
        found = resolve(reverse("products:result_search"))
        self.assertEqual(found.func, result_search)

    def test_product_sheet_url_view(self):
        found = resolve(reverse("products:product_sheet", kwargs={"code": 1}))
        self.assertEqual(found.func, product_sheet)

    def test_favorites_url_view(self):
        found = resolve(reverse("products:favorites"))
        self.assertEqual(found.func, favorites)

    def test_delete_favorites_url_view(self):
        found = resolve(reverse("products:delete_favorites"))
        self.assertEqual(found.func, delete_favorites)
