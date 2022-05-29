from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class MainPage(BasePage):
    OPENCART_LOGO = (By.CSS_SELECTOR, '#logo')
    SLIDESHOW = (By.CSS_SELECTOR, '#slideshow0')
    MACBOOK_IMG = (By.XPATH, '//div[contains(@class, "swiper-slide-active")]/img[@alt = "MacBookAir"]')
    IPHONE_IMG = (
        By.XPATH, '//div[contains(@class, "swiper-slide text-center swiper-slide-active")]/a/img[@alt = "iPhone 6"]')
    LAYOUT_PRODUCTS = (By.XPATH, '//div[contains(@class, "product-layout")]')
    SEARCH = (By.CSS_SELECTOR, '#search')
    CART_BUTTON = (By.CSS_SELECTOR, '#cart')
