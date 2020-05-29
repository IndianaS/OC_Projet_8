from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from products.openfoodfact.models.categorydownloader import CategoryDownloader
from products.models import Product
from sentry_sdk import capture_message
import logging


class Command(BaseCommand):
    help = 'Update data base'

    def handle(self, *args, **options):
        # Download the categories then the ranges
        category = CategoryDownloader()
        self.stdout.write('On télécharge les produits !')
        all_categories = category.get_category()
        for category in all_categories:
            for product in category.products:
                try:
                    db_product = Product.objects.get(id=product.id)
                except Product.DoesNotExist:
                    continue

                db_product.product_name_fr = product.product_name_fr
                db_product.stores = product.stores
                db_product.nutrition_grade_fr = product.nutrition_grade_fr
                db_product.id = product.id
                db_product.brands = product.brands
                db_product.url = product.url
                db_product.image_url = product.image_url
                db_product.image_nutrition_url = product.image_nutrition_url
                db_product.save()

        logging.info("Commande cron exécutée (DbUpdate)")
        capture_message("Commande cron exécutée (DbUpdate)", level="info")
