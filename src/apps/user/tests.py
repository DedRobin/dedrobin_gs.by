# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from faker import Faker

from src.apps.user.factories import UserFactory
from src.apps.user.models import CustomUser


class LoginTests(LiveServerTestCase):
    # fixtures = ["user-data.json"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.fake = Faker()
        cls.user: CustomUser = UserFactory()
        cls.user_password = cls.fake.md5()
        cls.user.set_password(cls.user_password)
        cls.user.save()
        cls.browser = WebDriver()
        cls.browser.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_login(self):
        self.browser.get(f"{self.live_server_url}")
        username_input = self.browser.find_element(By.NAME, "email")
        username_input.send_keys(self.user.email)
        password_input = self.browser.find_element(By.NAME, "password")
        password_input.send_keys(self.user_password)
        self.browser.find_element(By.CLASS_NAME, "btn-primary").click()
