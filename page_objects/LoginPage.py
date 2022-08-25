import json

from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')
    INVALID_LOGIN_ALERT = (By.CSS_SELECTOR, '.alert-danger')

    def login(self, user, login, password):
        with open('../../target.json') as json_file:
            data = json.load(json_file)
        self.browser.get(self.browser.current_url + '/index.php?route=account/login')
        self.browser.find_element(*self.EMAIL_INPUT).send_keys(data[f'{user}'][f'{login}'])
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(data[f'{user}'][f'{password}'])
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def get_login_alert(self):
        self.verify_element_present(LoginPage.INVALID_LOGIN_ALERT)
