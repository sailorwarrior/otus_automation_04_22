from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class SearchPage(BasePage):
    PRODUCT_NAMES = (By.CSS_SELECTOR, '.caption > h4 > a')

    def get_searched_items_names(self):
        elements_list = self.browser.find_elements(*SearchPage.PRODUCT_NAMES)
        list_of_names = []
        for el in elements_list:
            product_name = el.text
            list_of_names.append(product_name)
        return list_of_names
