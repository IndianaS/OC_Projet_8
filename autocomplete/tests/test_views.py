from django.test import TestCase
from django.urls import reverse
import json
from products.models import Category, Product


class AutocompleteViewsTestCase(TestCase):

    def setUp(self):
        category = Category.objects.create(name="pizza")
        Product.objects.create(
            id_category=category,
            product_name_fr="pizza jambon",
            id=1854796,
        )

    def test_views_autocomplete_complete(self):
        response = self.client.get(reverse("autocomplete:complete"), {
            "term" : "pizz"
        })
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, json.dumps(["pizza jambon"]))
