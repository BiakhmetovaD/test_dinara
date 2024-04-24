from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base_page import BasePage
from pages.base_page import random_user
import allure

login_button = (By.ID, 'login-button')
username_field = (By.ID, 'user-name')
password_field = (By.ID, 'password')
container_field = (By.ID, 'inventory_container')


class AuthorizationPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        with allure.step('Open browser'):
            self.browser.get('https://saucedemo.com')

    def login_button(self):
        with allure.step('Find the button'):
            return self.find(login_button)

    def login_button_click(self):
        with allure.step('Click button'):
            return self.login_button().click

    def username(self):
        with allure.step('Find the button'):
            return self.find(username_field)

    def username_click(self):
        with allure.step('Click button'):
            return self.username().click

    def username_send(self):
        with allure.step('Send username'):
            return self.username().send_keys(random_user())

    def password(self):
        with allure.step('Find the button'):
            return self.find(password_field)

    def password_click(self):
        with allure.step('Click button'):
            return self.password().click

    def password_send(self):
        with allure.step('Send password'):
            return self.password().send_keys('secret_sauce')

    def pause(self, sec: int):
        # self.browser.implicitly_wait(sec)
        sleep(sec)

    def assert_auth(self):
        assert self.find_elements(container_field)