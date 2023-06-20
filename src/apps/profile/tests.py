from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from faker import Faker
from selenium.webdriver.support.ui import Select

from src.apps.user.factories import UserFactory
from src.apps.profile.factories import ProfileFactory
from src.apps.user.models import CustomUser
from src.apps.profile.models import Profile


class ProfileTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.fake = Faker()
        cls.user: CustomUser = UserFactory()
        cls.user_password = cls.fake.md5()
        cls.user.set_password(cls.user_password)
        cls.user.save()
        cls.profile: Profile = ProfileFactory(user=cls.user)
        # Browser config
        cls.browser = WebDriver()
        cls.browser.implicitly_wait(5)
        cls.browser = cls.login(cls)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def login(self):
        self.browser.get(self.live_server_url)
        username_input = self.browser.find_element(By.NAME, "email")
        username_input.send_keys(self.user.email)
        password_input = self.browser.find_element(By.NAME, "password")
        password_input.send_keys(self.user_password)
        self.browser.find_element(By.CLASS_NAME, "btn-primary").click()
        assert self.browser.title == "DedRobin Game Service"
        return self.browser

    def test_edit_profile(self):
        xpath = '/html/body/nav/div/div/ul[2]/li/ul/li[1]/a'
        href = self.browser.find_element(By.XPATH, xpath).get_attribute("href")
        self.browser.get(href)
        assert self.browser.title == "Edit profile"

        # Updated data
        updated_user = UserFactory.build()
        updated_profile = ProfileFactory.build(user=updated_user)
        inputs = {
            "id_username": updated_user.username,
            "id_email": updated_user.email,
            "id_first_name": updated_profile.first_name,
            "id_last_name": updated_profile.last_name,
            "id_gender": updated_profile.gender,
            "id_phone_number": updated_profile.phone_number,
            "id_age": updated_profile.age,
            "id_birthday": updated_profile.birthday,
        }

        for input_id, data in inputs.items():
            one_input = self.browser.find_element(By.ID, input_id)
            if one_input.tag_name == "input":
                one_input.clear()
                one_input.send_keys(data)
            elif one_input.tag_name == "select":
                select = Select(one_input)
                select.select_by_visible_text(data)
            self.browser.find_element(By.XPATH, '/html/body/div[1]/div/form/button').click()
            message = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]').text
            assert message == "Your data has been updated"

        # Delete test
        xpath = "/html/body/div[1]/div/button"
        self.browser.find_element(By.XPATH, xpath).click()
        self.browser.find_element(By.NAME, "confirm_test").send_keys(f"{updated_user.email}-delete")
        conf_xpath = '/html/body/div[1]/div/div[4]/div/div/form/button[1]'
        self.browser.find_element(By.XPATH, conf_xpath).click()
        assert self.browser.title == "Login"
