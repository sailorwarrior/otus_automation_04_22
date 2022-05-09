from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework import amount_of_elements


class CatalogPageLocators:
    LEFT_MENU = (By.CSS_SELECTOR, '#column-left')
    LEFT_BANNER = (By.CSS_SELECTOR, '.swiper-viewport > #banner0')
    PRODUCTS = (By.CSS_SELECTOR, '.product-thumb')
    LIST_VIEW_BUTTON = (By.CSS_SELECTOR, '#list-view')
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, '#grid-view')
    SORTING_INPUT = (By.CSS_SELECTOR, '#input-sort')
    SORTING_OPTIONS_DROPDOWN = (By.CSS_SELECTOR, '#input-sort > option')


def test_main_page_header(browser, base_url):
    browser.get(f'{base_url}/desktops')
    assert "Desktops" == browser.title


def test_check_left_side(browser, base_url):
    browser.get(f'{base_url}/desktops')
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located(CatalogPageLocators.LEFT_BANNER))
    wait.until(EC.visibility_of_element_located(CatalogPageLocators.LEFT_MENU))


def test_check_products(browser, base_url):
    browser.get(f'{base_url}/desktops')
    wait = WebDriverWait(browser, 2)
    wait.until(amount_of_elements(CatalogPageLocators.PRODUCTS, 12))
    wait.until(EC.visibility_of_all_elements_located(CatalogPageLocators.PRODUCTS))


def test_check_view_buttons(browser, base_url):
    browser.get(f'{base_url}/desktops')
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located(CatalogPageLocators.LIST_VIEW_BUTTON))
    wait.until(EC.visibility_of_element_located(CatalogPageLocators.GRID_VIEW_BUTTON))


def test_check_sorting(browser, base_url):
    browser.get(f'{base_url}/desktops')
    sorting_input = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(CatalogPageLocators.SORTING_INPUT))
    sorting_input.click()
    WebDriverWait(browser, 2).until(EC.visibility_of_all_elements_located(CatalogPageLocators.SORTING_OPTIONS_DROPDOWN))
    WebDriverWait(browser, 2).until(amount_of_elements(CatalogPageLocators.SORTING_OPTIONS_DROPDOWN, 9))
