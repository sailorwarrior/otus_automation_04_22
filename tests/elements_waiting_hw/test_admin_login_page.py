from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminLoginPageLocators:
    USERNAME_INPUT = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//a[.="Forgotten Password"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type = "submit"]')


def test_check_admin_login_page(browser, base_url):
    browser.get(f'{base_url}/admin')
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located(AdminLoginPageLocators.USERNAME_INPUT))
    wait.until(EC.visibility_of_element_located(AdminLoginPageLocators.PASSWORD_INPUT))
    wait.until(EC.visibility_of_element_located(AdminLoginPageLocators.FORGOT_PASSWORD_BUTTON))
    wait.until(EC.visibility_of_element_located(AdminLoginPageLocators.SUBMIT_BUTTON))
