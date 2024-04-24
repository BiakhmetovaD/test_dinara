import random
from selenium.webdriver.chrome.webdriver import WebDriver


def random_user():
    login_list = ['standard_user', 'error_user', 'visual_user']
    return random.choice(login_list)


class BasePage:
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    def find_elements(self, args):
        return self.browser.find_elements(*args)
