import allure
from allure_commons.types import Severity

from page_objects.elements.Header import Header
from page_objects.RegistrationPage import RegistrationPage


@allure.title('Регистрация пользователя')
@allure.tag('Registration')
@allure.severity(severity_level=Severity.BLOCKER)
def test_user_registration(browser, base_url):
    header = Header(browser)
    registration_page = RegistrationPage(browser)

    with allure.step('Перейти на страницу регистрации'):
        header.my_account_open()
        header.register_button_click()
        registration_page.wait_for_form_elements()

    with allure.step('Заполнить данные и подтвердить регистрацию'):
        registration_page.fill_registration_form()
        registration_page.agree_privacy_checkbox_click()
        registration_page.submit_button_click()

    with allure.step('Проверить, успешна ли регистрация'):
        success_registration = registration_page.is_registration_successful()
    assert success_registration is True
