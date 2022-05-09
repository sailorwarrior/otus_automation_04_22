from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework import assert_element


class ProductCardPageLocators:
    MAIN_PHOTO = (By.CSS_SELECTOR, '.thumbnails > li:first-child > a')
    ADDITIONAL_PHOTOS = (By.CSS_SELECTOR, 'li.image-additional > a')
    NAVIGATION_TAB = (By.CSS_SELECTOR, '.nav-tabs')
    OPTION_SELECTOR = (By.CSS_SELECTOR, '#input-option2267')
    QUANTITY_INPUT = (By.CSS_SELECTOR, '#input-quantity')
    ADD_TO_WL_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title = "Add to Wish List"]')
    COMPARE_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title = "Compare this Product"]')


def test_check_product_photos(browser, base_url):
    browser.get(f'{base_url}/desktops/canon-eos-5d')
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located(ProductCardPageLocators.MAIN_PHOTO))
    wait.until(EC.visibility_of_all_elements_located(ProductCardPageLocators.ADDITIONAL_PHOTOS))


def test_check_navigation_tab(browser, base_url):
    browser.get(f'{base_url}/desktops/canon-eos-5d')
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(ProductCardPageLocators.NAVIGATION_TAB))


def test_check_options_block(browser, base_url):
    browser.get(f'{base_url}/desktops/canon-eos-5d')
    assert_element(ProductCardPageLocators.OPTION_SELECTOR, browser)
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(ProductCardPageLocators.QUANTITY_INPUT))


def test_check_buttons(browser, base_url):
    browser.get(f'{base_url}/desktops/canon-eos-5d')
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(ProductCardPageLocators.ADD_TO_WL_BUTTON))
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(ProductCardPageLocators.COMPARE_BUTTON))
