# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from faker import Faker

from src.apps.user.factories import UserFactory
from src.apps.user.models import CustomUser


class AuthTests(LiveServerTestCase):
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

    def test_registration(self):
        username = self.fake.user_name()
        email = self.fake.email()
        password = self.fake.md5()

        self.browser.get(f"{self.live_server_url}")
        register_xpath = '//*[@id="navbarSupportedContent"]/ul[2]/li[2]/a'
        register_href = self.browser.find_element(By.XPATH, register_xpath).get_attribute("href")
        self.browser.get(register_href)
        assert self.browser.title == "Registration"

        username_input = self.browser.find_element(By.NAME, "username")
        username_input.send_keys(username)
        email_input = self.browser.find_element(By.NAME, "email")
        email_input.send_keys(email)
        password1_input = self.browser.find_element(By.NAME, "password1")
        password1_input.send_keys(password)
        password2_input = self.browser.find_element(By.NAME, "password2")
        password2_input.send_keys(password)
        self.browser.find_element(By.CLASS_NAME, "btn-primary").click()
        assert self.browser.title == "Login"

    def test_login_and_logout(self):
        email = self.user.email
        password = self.user_password

        self.browser.get(f"{self.live_server_url}")
        username_input = self.browser.find_element(By.NAME, "email")
        username_input.send_keys(email)
        password_input = self.browser.find_element(By.NAME, "password")
        password_input.send_keys(password)
        self.browser.find_element(By.CLASS_NAME, "btn-primary").click()
        assert self.browser.title == "DedRobin Game Service"

        xpath = '/html/body/nav/div/div/ul[2]/li/ul/li[3]/a'
        href_logout = self.browser.find_element(By.XPATH, xpath).get_attribute("href")
        self.browser.get(href_logout)
        assert self.browser.title == "Login"
