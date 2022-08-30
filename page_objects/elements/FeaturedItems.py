import time

from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class FeaturedItems(BasePage):
    FEATURED_ITEMS_ADDING_LIST = (By.XPATH, '//button[contains(@onclick, "cart.add")]')
    FEATURED_ITEMS_WISHLIST = (By.XPATH, '//button[contains( @ onclick, "wishlist.add")]')

    def add_item_to_cart(self):
        elements_list = self.browser.find_elements(*self.FEATURED_ITEMS_ADDING_LIST)
        random_element = elements_list[1]
        random_element.click()
        time.sleep(5)

    def add_item_to_wish_list(self):
        elements_list = self.browser.find_elements(*self.FEATURED_ITEMS_WISHLIST)
        random_element = elements_list[1]
        random_element.click()
