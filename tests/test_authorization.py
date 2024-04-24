from time import sleep
from pages.authorization_page import AuthorizationPage
import allure


@allure.feature('Authorization')
@allure.story('Authorization to the system')
@allure.description('dsjfsfshkgjg1')
def test_authorization(browser):
    with allure.step('Open browser'):
        authorization_page = AuthorizationPage(browser)
    with allure.step('Go to site'):
        authorization_page.open()
    with allure.step('Write username'):
        authorization_page.username_send()
        sleep(1)
    with allure.step('Write password'):
        authorization_page.password_send()
        sleep(1)
    with allure.step('Click button'):
        authorization_page.login_button().click()
        sleep(1)


@allure.feature('Registration')
@allure.story('Registartion to the system')
def test_authorizationError(browser):
    with allure.step('Open browser'):
        authorization_page = AuthorizationPage(browser)
    with allure.step('Open browser'):
        authorization_page.open()
    with allure.step('Check the text'):
        assert "Loogin" == authorization_page.login_button().text
