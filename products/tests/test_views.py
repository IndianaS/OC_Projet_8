from django.test import TestCase

from products.models import Category, Favorite, Product
from users.models import User


class ProductTestViews(TestCase):

    def setUp(self):
        category = Category.objects.create(name="pizza")
        Product.objects.create(
            id=1854796,
            id_category=category,
            product_name_fr="pizza jambon",
            nutrition_grade_fr="b"
        )
        Product.objects.create(
            id=1254547,
            id_category=category,
            product_name_fr="pizza fromage",
            nutrition_grade_fr="a"
        )
        User.objects.create_user(
            username="UserTest", password="PaswordTest&120")

    def test_views_result_search(self):
        response = self.client.get('/products/?q=pizza')
        self.assertEqual(response.status_code, 200)

    def test_views_product_sheet(self):
        response = self.client.get('/products/details/1854796/')
        self.assertEqual(response.status_code, 200)

    def test_views_favorites(self):
        self.client.login(username="UserTest", password="PaswordTest&120")
        response = self.client.get('/users/favorites/')
        self.assertEqual(response.status_code, 200)

    def test_views_favorites_without_POST_method(self):
        response = self.client.get('/products/favorites')
        self.assertRedirects(response, '/', status_code=302)

    def test_views_favorites_with_POST_method(self):
        self.client.login(username="UserTest", password="PaswordTest&120")
        id_substitut = Product.objects.get(id=1254547).id
        id_product = Product.objects.get(id=1854796).id
        response = self.client.post(
            '/products/favorites',
            {
                "id_substitut": id_substitut,
                "id_product": id_product
            })
        favorite = Favorite.objects.get(
            product__id=1854796, substitute__id=1254547)

        self.assertEqual(favorite.product.id, id_product)
        self.assertRedirects(
            response, '/products/details/1254547/', status_code=302)

    def test_views_delete_favorites(self):
        self.client.login(username="UserTest", password="PaswordTest&120")
        response = self.client.get('/users/favorites/')
        self.assertEqual(response.status_code, 200)

    def test_views_delete_favorites_with_POST_method(self):
        self.client.login(username="UserTest", password="PaswordTest&120")
        user =  User.objects.get(username="UserTest")
        product = Product.objects.get(id=1254547)
        substitute = Product.objects.get(id=1854796)

        favorite_save = Favorite.objects.get_or_create(
            user=user,
            product=product,
            substitute=substitute
        )
        response = self.client.post(
            '/products/delete_favorites',
            {
                "id_substitute": substitute.id
            })

        self.assertEqual(Favorite.objects.count(), 0)
        self.assertRedirects(
            response, '/users/favorites/', status_code=302)
