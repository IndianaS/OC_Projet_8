from django.test import TestCase
from django.urls import reverse
import json


class AutocompleteViews(TestCase):

    def test_views_autocomplete_complete(self):
        response = self.client.get(reverse("autocomplete/complete", {
            "term" : "pizz"
        }))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, json.dumps("pizza"))
