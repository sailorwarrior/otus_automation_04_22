from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AdminProductsPage(BasePage):
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, '.fa-plus')
    FILTER_NAME_INPUT = (By.CSS_SELECTOR, 'input[name="filter_name"]')
    FILTER_BUTTON = (By.CSS_SELECTOR, '#button-filter')
    PRODUCTS_COUNT_TEXT = (By.CSS_SELECTOR, '.panel-body > div > div:last-child')
    PRODUCT_NAME_TEXT = (By.CSS_SELECTOR, 'tbody > tr > td:nth-child(3)')
    LAST_CHECKBOX = (By.CSS_SELECTOR,
                     '.table-hover > tbody > tr:last-child > .text-center > input[type = "checkbox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, '.btn-danger')

    def add_new_product_click(self):
        self.browser.find_element(*self.ADD_PRODUCT_BUTTON).click()

    def filter_product_by_name(self, product_name):
        self.browser.find_element(*self.FILTER_NAME_INPUT).send_keys(product_name)
        self.browser.find_element(*self.FILTER_BUTTON).click()

    def products_count_get(self):
        products_counter_text = self.browser.find_element(*self.PRODUCTS_COUNT_TEXT).text
        products_counter_text_splited = products_counter_text.split()
        products_count = int(products_counter_text_splited[-3])
        return products_count

    def product_names_get(self):
        product_names = self.browser.find_elements(*self.PRODUCT_NAME_TEXT)
        return product_names

    def last_checkbox_in_list_click(self):
        self.browser.find_element(*self.LAST_CHECKBOX).click()

    def delete_button_click(self):
        self.browser.find_element(*self.DELETE_BUTTON).click()
