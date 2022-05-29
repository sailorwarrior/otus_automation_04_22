from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class CatalogPage(BasePage):
    LEFT_MENU = (By.CSS_SELECTOR, '#column-left')
    LEFT_BANNER = (By.CSS_SELECTOR, '.swiper-viewport > #banner0')
    PRODUCTS = (By.CSS_SELECTOR, '.product-thumb')
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, '#list-view')
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, '#grid-view')
    SORTING_INPUT = (By.CSS_SELECTOR, '#input-sort')
    SORTING_OPTIONS_DROPDOWN = (By.CSS_SELECTOR, '#input-sort > option')
