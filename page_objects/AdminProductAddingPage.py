from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AdminProductAddingPage(BasePage):
    NAME_INPUT = (By.CSS_SELECTOR, '#input-name1')
    METATAG_INPUT = (By.CSS_SELECTOR, '#input-meta-title1')
    DATA_TAB = (By.CSS_SELECTOR, 'a[href = "#tab-data"]')
    MODEL_INPUT = (By.CSS_SELECTOR, '#input-model')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type = "submit"]')

    def fill_general_product_info(self, product_name, meta_tag):
        self.browser.find_element(*self.NAME_INPUT).send_keys(product_name)
        self.browser.find_element(*self.METATAG_INPUT).send_keys(meta_tag)

    def data_tab_click(self):
        self.browser.find_element(*self.DATA_TAB).click()

    def fill_data_product_info(self, model):
        self.browser.find_element(*self.MODEL_INPUT).send_keys(model)

    def submit_adding_product_button_click(self):
        self.browser.find_element(*self.SUBMIT_BUTTON).click()
