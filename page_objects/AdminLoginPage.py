import json
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from pathlib import Path


class AdminLoginPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type = "submit"]')
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//a[.="Forgotten Password"]')

    def login(self):
        self.logger.info('Go to admin page')
        myself = Path(__file__).resolve()
        res = myself.parents[1] / 'target.json'
        with open(res) as json_file:
            data = json.load(json_file)
        self.browser.get(self.browser.current_url + 'admin')
        self.verify_element_present(AdminLoginPage.USERNAME_INPUT)
        self.verify_element_present(AdminLoginPage.PASSWORD_INPUT)
        self.verify_element_present(AdminLoginPage.FORGOT_PASSWORD_BUTTON)
        self.verify_element_present(AdminLoginPage.LOGIN_BUTTON)
        self.logger.info('Login data input')
        self.browser.find_element(*self.USERNAME_INPUT).send_keys(data['admin']['login'])
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(data['admin']['password'])
        self.logger.info('Login button click')
        self.browser.find_element(*self.LOGIN_BUTTON).click()
