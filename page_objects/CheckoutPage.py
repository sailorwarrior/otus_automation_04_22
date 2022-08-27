import time

from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class CheckoutPage(BasePage):
    ADDRESS_INPUT = (By.CSS_SELECTOR, 'select[name="address_id"]')
    STEP_TWO_CONTINUE_BUTTON = (By.CSS_SELECTOR, '.pull-right > #button-payment-address')
    DELIVERY_INPUT = (By.CSS_SELECTOR, '.form-horizontal > #shipping-existing')
    STEP_THREE_CONTINUE_BUTTON = (By.CSS_SELECTOR, '.pull-right > #button-shipping-address')
    STEP_FOUR_CONTINUE_BUTTON = (By.CSS_SELECTOR, '.pull-right > #button-shipping-method')
    STEP_FIVE_CONTINUE_BUTTON = (By.CSS_SELECTOR, '.pull-right > #button-payment-method')
    TERMS_AGREE_CHECKBOX = (By.CSS_SELECTOR, 'input[type="checkbox"]')
    CONFIRM_BUTTON = (By.CSS_SELECTOR, '.pull-right > #button-confirm')
    SUCCESS_ORDER_HEADER = (By.CSS_SELECTOR, '#content > h1')
    ADD_NEW_ADDRESS_RADIO = (By.CSS_SELECTOR, 'input[value="new"]')
    INPUT_PAYMENT_FIRSTNAME = (By.CSS_SELECTOR, '#input-payment-firstname')
    INPUT_PAYMENT_LASTNAME = (By.CSS_SELECTOR, '#input-payment-lastname')
    INPUT_ADDRESS_ONE = (By.CSS_SELECTOR, '#input-payment-address-1')
    INPUT_PAYMENT_CITY = (By.CSS_SELECTOR, '#input-payment-city')
    INPUT_PAYMENT_POSTCODE = (By.CSS_SELECTOR, '#input-payment-postcode')
    INPUT_PAYMENT_ZONE = (By.CSS_SELECTOR, '#input-payment-zone')
    INPUT_PAYMENT_ZONE_CHOOSE = (By.CSS_SELECTOR, '#input-payment-zone > option[value = "3513"]')

    def fill_checkout_form(self, add_new_address):
        self.verify_element_present(CheckoutPage.STEP_TWO_CONTINUE_BUTTON)
        if add_new_address is True:
            self.browser.find_element(*self.ADD_NEW_ADDRESS_RADIO).click()
            self.fill_address_in_checkout('test', 'test')

        self.browser.find_element(*self.STEP_TWO_CONTINUE_BUTTON).click()
        self.verify_element_present(CheckoutPage.STEP_THREE_CONTINUE_BUTTON).click()
        self.verify_element_present(CheckoutPage.STEP_FOUR_CONTINUE_BUTTON).click()
        self.verify_element_present(self.TERMS_AGREE_CHECKBOX).click()
        self.verify_element_present(CheckoutPage.STEP_FIVE_CONTINUE_BUTTON).click()
        self.verify_element_present(CheckoutPage.CONFIRM_BUTTON).click()

    def fill_address_in_checkout(self, firstname, lastname):
        self.browser.find_element(*self.INPUT_PAYMENT_FIRSTNAME).send_keys(firstname)
        self.browser.find_element(*self.INPUT_PAYMENT_LASTNAME).send_keys(lastname)
        self.browser.find_element(*self.INPUT_ADDRESS_ONE).send_keys(lastname)
        self.browser.find_element(*self.INPUT_PAYMENT_CITY).send_keys(lastname)
        self.browser.find_element(*self.INPUT_PAYMENT_POSTCODE).send_keys(lastname)
        self.browser.find_element(*self.INPUT_PAYMENT_ZONE_CHOOSE).click()

    def wait_for_successful_order(self, url):
        self.wait_for_urt_to_change(current_url=url)
        self.verify_element_present(CheckoutPage.SUCCESS_ORDER_HEADER)
