from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class WishlistPage(BasePage):
    DELETE_BUTTONS_LIST = (By.XPATH, '//a[@data-original-title="Remove"]')
    ALERT_SUCCESS = (By.CSS_SELECTOR, '.alert-success')

    def delete_items_from_wishlist(self):
        delete_buttons_list = self.browser.find_elements(*WishlistPage.DELETE_BUTTONS_LIST)
        if len(delete_buttons_list) > 0:
            for el in delete_buttons_list:
                el.click()
                self.verify_element_present(WishlistPage.ALERT_SUCCESS)
        else:
            pass
