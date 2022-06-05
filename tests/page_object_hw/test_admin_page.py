from page_objects.AdminLoginPage import AdminLoginPage
from page_objects.AdminMainPage import AdminMainPage
from page_objects.AdminProductsPage import AdminProductsPage
from page_objects.AdminProductAddingPage import AdminProductAddingPage


def test_add_new_item(browser, base_url):
    admin_login_page = AdminLoginPage(browser)
    admin_main_page = AdminMainPage(browser)
    admin_products_page = AdminProductsPage(browser)
    admin_product_adding_page = AdminProductAddingPage(browser)

    product_name = f'Test Product {browser.session_id}'
    meta_tag = f'Test Meta Tag {browser.session_id}'
    model = f'Test Model Input {browser.session_id}'

    admin_login_page.login()
    admin_main_page.open_products_catalog()
    admin_products_page.add_new_product_click()
    admin_product_adding_page.fill_general_product_info(product_name=product_name, meta_tag=meta_tag)
    admin_product_adding_page.data_tab_click()
    admin_product_adding_page.fill_data_product_info(model=model)
    admin_product_adding_page.submit_adding_product_button_click()
    admin_products_page.filter_product_by_name(product_name)

    product_name_list = admin_products_page.product_names_get()

    filtered_product_name = product_name_list[0].text
    assert filtered_product_name == product_name


def test_delete_product(browser, base_url):
    admin_login_page = AdminLoginPage(browser)
    admin_main_page = AdminMainPage(browser)
    admin_products_page = AdminProductsPage(browser)

    admin_login_page.login()
    admin_main_page.open_products_catalog()

    previous_products_count = admin_products_page.products_count_get()

    admin_products_page.last_checkbox_in_list_click()
    admin_products_page.delete_button_click()
    browser.switch_to.alert.accept()

    current_products_count = admin_products_page.products_count_get()

    assert previous_products_count - current_products_count == 1
