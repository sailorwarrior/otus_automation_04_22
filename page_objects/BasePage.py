import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger

    @allure.step
    def verify_element_present(self, locator):
        self.logger.info(f'Waiting for element {locator[1]}')
        try:
            return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f'Element with locator {locator} is not found.')

    def wait_for_urt_to_change(self, current_url):
        WebDriverWait(self.browser, 5).until(EC.url_changes(current_url))
