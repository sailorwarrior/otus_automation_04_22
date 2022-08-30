import allure
from allure_commons.types import Severity

from page_objects.LoginPage import LoginPage


@allure.title('Валидный логин')
@allure.severity(severity_level=Severity.CRITICAL)
def test_valid_login(browser, base_url):
    login_page = LoginPage(browser)

    with allure.step('Перейти на страницу регистрации и ввести валидные логин и пароль'):
        login_page.login('valid_user', 'login', 'password')
    assert browser.current_url == f'{base_url}/index.php?route=account/account'


@allure.title('Невалидный логин')
@allure.severity(severity_level=Severity.CRITICAL)
def test_invalid_login(browser, base_url):
    login_page = LoginPage(browser)

    with allure.step('Перейти на страницу регистрации и ввести невалидные логин и пароль'):
        login_page.login('valid_user', 'login', 'invalid_password')

    with allure.step('Проверить наличие предупреждения о неуспешном логине'):
        login_page.get_login_alert()
    assert browser.current_url == f'{base_url}/index.php?route=account/login'
