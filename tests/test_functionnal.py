from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('window-size=1920x1080')


class ChromeFunctionalTestCases(StaticLiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get(self.live_server_url)

        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        User = get_user_model()
        User.objects.create_user(
            username="UserTest", password="PasswordTest&2003")

    def test_user_can_connect_and_disconnect(self):
        self.driver.find_element_by_css_selector('#button-login').click()
        self.driver.find_element_by_css_selector(
            '#id_username').send_keys("UserTest")
        self.driver.find_element_by_css_selector(
            '#id_password').send_keys("PasswordTest&2003")
        self.driver.find_element_by_css_selector('#button-submit').click()
        logout = self.driver.find_element_by_css_selector('#icon-logout')
        logout_classes = logout.get_attribute("class")
        self.assertIn("fa-sign-out-alt", logout_classes,
                      "Disconnect icon should be available.")
