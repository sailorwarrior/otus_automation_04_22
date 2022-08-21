from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPageLocators:
    OPENCART_LOGO = (By.CSS_SELECTOR, '#logo')
    SLIDESHOW = (By.CSS_SELECTOR, '#slideshow0')
    MACBOOK_IMG = (By.XPATH, '//div[contains(@class, "swiper-slide-active")]/img[@alt = "MacBookAir"]')
    IPHONE_IMG = (
        By.XPATH, '//div[contains(@class, "swiper-slide text-center swiper-slide-active")]/a/img[@alt = "iPhone 6"]')
    LAYOUT_PRODUCTS = (By.XPATH, '//div[contains(@class, "product-layout")]')
    SEARCH = (By.CSS_SELECTOR, '#search')
    CART_BUTTON = (By.CSS_SELECTOR, '#cart')


def test_main_page_header(browser, base_url):
    browser.get(base_url)
    assert "Your Store" == browser.title


def test_check_logo(browser, base_url):
    browser.get(base_url)
    logo = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPageLocators.OPENCART_LOGO))
    logo.click()
    assert browser.current_url == f'{base_url}/index.php?route=common/home'


def test_check_slideshow(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located(MainPageLocators.SLIDESHOW))
    wait.until(EC.visibility_of_element_located(MainPageLocators.IPHONE_IMG))
    wait.until(EC.visibility_of_element_located(MainPageLocators.MACBOOK_IMG))


def test_check_featured_products(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, 2)
    wait.until(EC.presence_of_all_elements_located(MainPageLocators.LAYOUT_PRODUCTS))
    wait.until(EC.visibility_of_all_elements_located(MainPageLocators.LAYOUT_PRODUCTS))


def test_check_search(browser, base_url):
    browser.get(base_url)
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPageLocators.SEARCH))


def test_check_cart(browser, base_url):
    browser.get(base_url)
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPageLocators.CART_BUTTON))
