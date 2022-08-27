import allure
import pytest
from allure_commons.types import Severity

from framework import assert_every_el_in_list_has_substring
from page_objects.CheckoutPage import CheckoutPage
from page_objects.LoginPage import LoginPage
from page_objects.SearchPage import SearchPage
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
        login.login(user='valid_user', login='login', password='password')
        header.click_on_logo()

    with allure.step('Добавление рандомного продукта из ленты в корзину'):
        previous_quantity = header.get_items_quantity_cart()
        featured.add_item_to_cart()
        header.wait_for_successful_alert()
        new_quantity = header.get_items_quantity_cart()
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
        header.open_wishlist()
        wishlist.delete_items_from_wishlist()

    with allure.step('Добавление рандомного продукта из ленты в вишлист'):
        header.click_on_logo()
        previous_quantity = header.get_items_quantity_wishlist()
        featured.add_item_to_wish_list()
        header.wait_for_successful_alert()
        new_quantity = header.get_items_quantity_wishlist()
    assert new_quantity - previous_quantity == 1


@allure.title('Быстрый поиск')
@allure.severity(severity_level=Severity.CRITICAL)
def test_fast_search(browser, db_connector):
    header = Header(browser)
    search = SearchPage(browser)

    with allure.step('Ввод наименования товара и нажатие на кнопку поиска'):
        product_to_find = db_connector.get_last_product_name()
        header.fast_search(product_to_find)

    with allure.step('Проверка, что продукт найден коррекнто'):
        searched_items_names = search.get_searched_items_names()
    assert_every_el_in_list_has_substring(list_of_items=searched_items_names, substring=product_to_find)


@allure.title('Проверка заголовка страницы')
@allure.severity(severity_level=Severity.MINOR)
def test_title_check(browser, base_url):
    browser.get(base_url)
    assert "Your Store" == browser.title


@allure.title('Оформление заказа')
@allure.severity(severity_level=Severity.MINOR)
@pytest.mark.parametrize('new_address', [True, False])
def test_checkout_check(browser, base_url, new_address):
    header = Header(browser)
    login = LoginPage(browser)
    featured = FeaturedItems(browser)
    checkout = CheckoutPage(browser)

    with allure.step('Предусловие. Валидный логин и переход на главную'):
        login.login('valid_user', 'login', 'password')
        header.click_on_logo()

    with allure.step('Предусловие. Добавление товара в корзину. Переход в чекаут'):
        featured.add_item_to_cart()
        header.open_checkout()

    with allure.step('Заполнение формы заказа'):
        allure.dynamic.title(f'Добавить новый адрес: {new_address}')
        checkout.fill_checkout_form(add_new_address=new_address)

    with allure.step('Проверка того, что заказ успешно оформлен'):
        checkout.wait_for_successful_order(browser.current_url)
    assert browser.current_url == f'{base_url}/index.php?route=checkout/success'
