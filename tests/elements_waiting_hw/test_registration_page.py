from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPageLocators:
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, '#input-firstname')
    LASTNAME_INPUT = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_NINPUT = (By.CSS_SELECTOR, '#input-email')
    PHONE_INPUT = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, '#input-confirm')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'input[type = "submit"]')


def test_check_registration_page(browser, base_url):
    browser.get(f'{base_url}/index.php?route=account/register')
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located(RegistrationPageLocators.FIRSTNAME_INPUT))
    wait.until(EC.visibility_of_element_located(RegistrationPageLocators.LASTNAME_INPUT))
    wait.until(EC.visibility_of_element_located(RegistrationPageLocators.EMAIL_NINPUT))
    wait.until(EC.visibility_of_element_located(RegistrationPageLocators.PHONE_INPUT))
    wait.until(EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_INPUT))
    wait.until(EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_CONFIRM_INPUT))
    wait.until(EC.visibility_of_element_located(RegistrationPageLocators.SUBMIT_BUTTON))
