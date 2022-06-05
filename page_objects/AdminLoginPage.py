import json
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AdminLoginPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type = "submit"]')
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//a[.="Forgotten Password"]')

    def login(self):
        with open('../../target.json') as json_file:
            data = json.load(json_file)
        self.browser.get(self.browser.current_url + 'admin')
        self.verify_element_present(AdminLoginPage.USERNAME_INPUT)
        self.verify_element_present(AdminLoginPage.PASSWORD_INPUT)
        self.verify_element_present(AdminLoginPage.FORGOT_PASSWORD_BUTTON)
        self.verify_element_present(AdminLoginPage.LOGIN_BUTTON)
        self.browser.find_element(*self.USERNAME_INPUT).send_keys(data['admin']['login'])
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(data['admin']['password'])
        self.browser.find_element(*self.LOGIN_BUTTON).click()
