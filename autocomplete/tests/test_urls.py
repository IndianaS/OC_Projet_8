from django.test import TestCase
from django.urls import resolve
from django.shortcuts import reverse

from autocomplete.views import complete


class UrlTestCase(TestCase):

    def test_complete_url_view(self):
        found = resolve(reverse("autocomplete:complete"))
        self.assertEqual(found.func, complete)
