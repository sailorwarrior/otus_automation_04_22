from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class Header(BasePage):
    MY_ACCOUNT_DROPDOWN = (By.CSS_SELECTOR, 'a[title="My Account"]')
    REGISTER_BUTTON = (By.XPATH, '//ul[@class = "dropdown-menu dropdown-menu-right" ]/li/a[text() = "Register"]')
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, '#form-currency')
    CURRENCY_VALUE = (By.CSS_SELECTOR, '#form-currency > div > button > strong')
    CURRENCY_EUR = (By.CSS_SELECTOR, 'button[name="EUR"]')
    CURRENCY_GBP = (By.CSS_SELECTOR, 'button[name="GBP"]')
    CURRENCY_USD = (By.CSS_SELECTOR, 'button[name="USD"]')

    def my_account_open(self):
        self.browser.find_element(*Header.MY_ACCOUNT_DROPDOWN).click()

    def register_button_click(self):
        self.browser.find_element(*Header.REGISTER_BUTTON).click()

    def currency_dropdown_click(self):
        self.browser.find_element(*Header.CURRENCY_DROPDOWN).click()

    def currency_value_get(self):
        currency_value = self.browser.find_element(*Header.CURRENCY_VALUE).text
        return currency_value

    def change_currency_and_get_new_value(self, index=0):
        currency_list = [self.CURRENCY_EUR, self.CURRENCY_USD, self.CURRENCY_GBP]
        button = currency_list[index]
        currency_value_button = self.browser.find_element(*button)
        currency_to_change = currency_value_button.text
        currency_to_change_value = currency_to_change[0]
        currency_value_button.click()
        return currency_to_change_value
