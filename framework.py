from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def amount_of_elements(locator, amount):
    def __predicate(driver):
        elements = driver.find_elements(*locator)
        if len(elements) == amount:
            if len(elements) == 0:
                return True
            return elements if amount > 1 else elements[0]
        else:
            raise AssertionError(f"Error while loading of {amount} elements with locator '{locator}'")

    return __predicate


def assert_element(locator, driver, timeout=1):
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    except TimeoutException:
        driver.save_screenshot(f"{driver.session_id}.png")
        raise AssertionError(f"Элемент с селектором '{locator[1]}' не найден")


def assert_every_el_in_list_has_substring(list_of_items, substring):
    if len(list_of_items) > 0:
        for element in list_of_items:
            if substring in element:
                pass
            else:
                raise AssertionError(f"Результат поиска {element} не содержит строку {substring}")
    else:
        raise AssertionError('В результате работы метода венрулся пустой список')
