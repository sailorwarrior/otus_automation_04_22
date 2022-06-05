import pytest
from page_objects.elements.Header import Header


@pytest.mark.parametrize('currency', [0, 1, 2])
def test_change_currency(browser, currency):
    header = Header(browser)
    header.currency_dropdown_click()
    changing_currency = header.change_currency_and_get_new_value(currency)
    current_currency = header.currency_value_get()
    assert changing_currency == current_currency
