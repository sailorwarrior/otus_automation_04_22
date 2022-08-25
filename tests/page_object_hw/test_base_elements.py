import time

import allure
import pytest
from allure_commons.types import Severity

from page_objects.LoginPage import LoginPage
from page_objects.WishlistPage import WishlistPage
from page_objects.elements.FeaturedItems import FeaturedItems
from page_objects.elements.Header import Header


@allure.title('Изменение валюты')
@allure.severity(severity_level=Severity.NORMAL)
@pytest.mark.parametrize('currency', [(0, 'eur'), (1, 'usd'), (2, 'dbp')], ids=['eur', 'usd', 'gbp'])
def test_change_currency(browser, currency):
    header = Header(browser)
    header.currency_dropdown_click()
    allure.dynamic.title(f'Изменить валюту на {currency[1]}')
    with allure.step(f'Поменять валюту на {currency[1]}'):
        changing_currency = header.change_currency_and_get_new_value(currency[0])

    with allure.step(f'Проверить изменение валюты на {currency[1]}'):
        current_currency = header.currency_value_get()
    assert changing_currency == current_currency


@allure.title('Добавление товара в корзину')
@allure.severity(severity_level=Severity.CRITICAL)
def test_add_item_to_cart(browser):
    header = Header(browser)
    featured = FeaturedItems(browser)
    login = LoginPage(browser)

    with allure.step('Предусловие. Валидный логин и переход на главную'):
        login.login('valid_user', 'login', 'password')
        header.click_on_logo()

    with allure.step('Добавление рандомного продукта из ленты в корзину'):
        previous_quantity = int(header.get_items_quantity_cart())
        featured.add_item_to_cart()
        header.wait_for_successful_alert()
        new_quantity = int(header.get_items_quantity_cart())
    assert new_quantity - previous_quantity == 1


@allure.title('Добавление товара в вишлист')
@allure.severity(severity_level=Severity.CRITICAL)
def test_add_item_to_wishlist(browser):
    header = Header(browser)
    featured = FeaturedItems(browser)
    login = LoginPage(browser)
    wishlist = WishlistPage(browser)

    with allure.step('Предусловие. Валидный логин и переход на главную'):
        login.login('valid_user', 'login', 'password')
        header.click_on_logo()

    with allure.step('Предусловие. Удаление всех продуктов из вишлиста'):
        wishlist.delete_items_from_wishlist()

    with allure.step('Добавление рандомного продукта из ленты в вишлист'):
        previous_quantity = int(header.get_items_quantity_wishlist())
        featured.add_item_to_wish_list()
        header.wait_for_successful_alert()
        new_quantity = int(header.get_items_quantity_wishlist())
    assert new_quantity - previous_quantity == 1
