from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class ProductCardPage(BasePage):
    MAIN_PHOTO = (By.CSS_SELECTOR, '.thumbnails > li:first-child > a')
    ADDITIONAL_PHOTOS = (By.CSS_SELECTOR, 'li.image-additional > a')
    NAVIGATION_TAB = (By.CSS_SELECTOR, '.nav-tabs')
    OPTION_SELECTOR = (By.CSS_SELECTOR, '#input-option226')
    QUANTITY_INPUT = (By.CSS_SELECTOR, '#input-quantity')
    ADD_TO_WL_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title = "Add to Wish List"]')
    COMPARE_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title = "Compare this Product"]')
