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
    CART_BUTTON = (By.CSS_SELECTOR, '#cart')
    CART_ITEM_QUANTITY = (By.CSS_SELECTOR, '#cart-total')
    OPENCART_LOGO = (By.CSS_SELECTOR, '#logo')
    SUCCESSFULLY_ADDED_ALERT = (By.CSS_SELECTOR, '.alert-success')
    WISHLIST_BUTTON = (By.CSS_SELECTOR, '#wishlist-total')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[name="search"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.fa-search')

    def my_account_open(self):
        self.logger.info('My account opening')
        self.browser.find_element(*Header.MY_ACCOUNT_DROPDOWN).click()

    def register_button_click(self):
        self.browser.find_element(*Header.REGISTER_BUTTON).click()

    def currency_dropdown_click(self):
        self.browser.find_element(*Header.CURRENCY_DROPDOWN).click()

    def currency_value_get(self):
        currency_value = self.browser.find_element(*Header.CURRENCY_VALUE).text
        return currency_value

    def change_currency_and_get_new_value(self, index=0):
        self.logger.info('Currency changing')
        currency_list = [self.CURRENCY_EUR, self.CURRENCY_USD, self.CURRENCY_GBP]
        button = currency_list[index]
        currency_value_button = self.browser.find_element(*button)
        currency_to_change = currency_value_button.text
        currency_to_change_value = currency_to_change[0]
        currency_value_button.click()
        return currency_to_change_value

    def open_cart(self):
        self.browser.find_element(*Header.CART_BUTTON).click()

    def get_items_quantity_cart(self):
        items_quantity = self.browser.find_element(*Header.CART_ITEM_QUANTITY)
        items_quantity_text = items_quantity.text
        splited_quantity_text = items_quantity_text.split()
        count = splited_quantity_text[0]
        return count

    def click_on_logo(self):
        self.browser.find_element(*Header.OPENCART_LOGO).click()

    def wait_for_successful_alert(self):
        self.verify_element_present(Header.SUCCESSFULLY_ADDED_ALERT)

    def get_items_quantity_wishlist(self):
        items_quantity = self.browser.find_element(*Header.WISHLIST_BUTTON)
        items_quantity_text = items_quantity.text
        splited_quantity_text = items_quantity_text.split('(')
        count = splited_quantity_text[1][0:-1]
        return count

    def delete_items_from_wishlist(self):
        self.browser.find_element(*Header.WISHLIST_BUTTON).click()

    def fast_search(self, input_value):
        test1 = self.browser.find_element(*Header.SEARCH_INPUT)
        test1.click()
        test1.send_keys(input_value)
        self.browser.find_element(*Header.SEARCH_BUTTON).click()
