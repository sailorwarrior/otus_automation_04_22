import random

from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class RegistrationPage(BasePage):
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, '#input-firstname')
    LASTNAME_INPUT = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_NINPUT = (By.CSS_SELECTOR, '#input-email')
    PHONE_INPUT = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, '#input-confirm')
    AGREE_POLICY_CHECKBOX = (By.CSS_SELECTOR, 'input[name = "agree"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'input[type = "submit"]')
    SUCCESS_REGISTRATION_MESSAGE = (By.CSS_SELECTOR, '#content > h1')

    def wait_for_form_elements(self):
        elements_list = [RegistrationPage.FIRSTNAME_INPUT, RegistrationPage.LASTNAME_INPUT,
                         RegistrationPage.EMAIL_NINPUT, RegistrationPage.PHONE_INPUT, RegistrationPage.PASSWORD_INPUT,
                         RegistrationPage.PASSWORD_CONFIRM_INPUT, RegistrationPage.AGREE_POLICY_CHECKBOX,
                         RegistrationPage.SUBMIT_BUTTON]
        for element in elements_list:
            self.verify_element_present(element)

    def fill_registration_form(self):
        random_list = random.sample(range(0, 9), 9)
        random_str = ''.join([str(item) for item in random_list])
        self.browser.find_element(*RegistrationPage.FIRSTNAME_INPUT).send_keys('firstname')
        self.browser.find_element(*RegistrationPage.LASTNAME_INPUT).send_keys('lastname')
        self.browser.find_element(*RegistrationPage.EMAIL_NINPUT).send_keys(f'{self.browser.session_id}@mail.ru')
        self.browser.find_element(*RegistrationPage.PHONE_INPUT).send_keys(f'89{random_str}')
        self.browser.find_element(*RegistrationPage.PASSWORD_INPUT).send_keys(f'pass{self.browser.session_id}')
        self.browser.find_element(*RegistrationPage.PASSWORD_CONFIRM_INPUT).send_keys(f'pass{self.browser.session_id}')

    def agree_privacy_checkbox_click(self):
        self.browser.find_element(*RegistrationPage.AGREE_POLICY_CHECKBOX).click()

    def submit_button_click(self):
        self.browser.find_element(*RegistrationPage.SUBMIT_BUTTON).click()

    def is_registration_successful(self):
        success_text = self.browser.find_element(*RegistrationPage.SUCCESS_REGISTRATION_MESSAGE).text
        if success_text == 'Your Account Has Been Created!':
            return True
        else:
            return False
