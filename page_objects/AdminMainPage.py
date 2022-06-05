from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AdminMainPage(BasePage):
    CATALOG_DROPDOWN = (By.CSS_SELECTOR, '#menu-catalog')
    PRODUCTS_BUTTON = (By.XPATH, '//a[text() = "Products"]')

    def open_products_catalog(self):
        self.browser.find_element(*self.CATALOG_DROPDOWN).click()
        self.browser.find_element(*self.PRODUCTS_BUTTON).click()
