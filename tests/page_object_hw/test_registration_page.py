from page_objects.elements.Header import Header
from page_objects.RegistrationPage import RegistrationPage


def test_user_registration(browser, base_url):
    header = Header(browser)
    registration_page = RegistrationPage(browser)

    header.my_account_open()
    header.register_button_click()
    registration_page.wait_for_form_elements()
    registration_page.fill_registration_form()
    registration_page.agree_privacy_checkbox_click()
    registration_page.submit_button_click()
    success_registration = registration_page.is_registration_successful()
    assert success_registration is True
