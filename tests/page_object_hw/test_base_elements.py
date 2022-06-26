import allure
import pytest
from allure_commons.types import Severity

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
