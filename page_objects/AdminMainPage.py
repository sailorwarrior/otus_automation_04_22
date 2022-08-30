from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AdminMainPage(BasePage):
    CATALOG_DROPDOWN = (By.CSS_SELECTOR, '#menu-catalog')
    PRODUCTS_BUTTON = (By.XPATH, '//a[text() = "Products"]')
    TOTAL_ORDERS_COUNT = (By.CSS_SELECTOR, '.row> div:first-child > .tile-primary>.tile-body>h2')
    TOTAL_CUSTOMERS = (By.CSS_SELECTOR, '.row> div:nth-child(3) > .tile-primary>.tile-body>h2')

    def open_products_catalog(self):
        self.logger.info('Catalog page opening')
        self.browser.find_element(*self.CATALOG_DROPDOWN).click()
        self.browser.find_element(*self.PRODUCTS_BUTTON).click()

    def get_orders_count(self):
        count = self.browser.find_element(*self.TOTAL_ORDERS_COUNT)
        count_text = count.text
        return int(count_text)

    def get_customers_count(self):
        count = self.browser.find_element(*self.TOTAL_CUSTOMERS)
        count_text = count.text
        return int(count_text)
