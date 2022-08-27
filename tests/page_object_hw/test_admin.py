import allure
from allure_commons.types import Severity

from page_objects.AdminLoginPage import AdminLoginPage
from page_objects.AdminMainPage import AdminMainPage
from page_objects.AdminProductsPage import AdminProductsPage
from page_objects.AdminProductAddingPage import AdminProductAddingPage


@allure.title('Добавление нового товара админом')
@allure.severity(severity_level=Severity.CRITICAL)
def test_add_new_item(browser, base_url):
    admin_login_page = AdminLoginPage(browser)
    admin_main_page = AdminMainPage(browser)
    admin_products_page = AdminProductsPage(browser)
    admin_product_adding_page = AdminProductAddingPage(browser)

    product_name = f'Test Product {browser.session_id}'
    meta_tag = f'Test Meta Tag {browser.session_id}'
    model = f'Test Model Input {browser.session_id}'

    with allure.step('Логин под админом и переход в Каталог'):
        admin_login_page.login()
        admin_main_page.open_products_catalog()
        admin_products_page.add_new_product_click()

    with allure.step(f'Заполнить информацию о продукте {product_name}'):
        admin_product_adding_page.fill_general_product_info(product_name=product_name, meta_tag=meta_tag)
        admin_product_adding_page.data_tab_click()
        admin_product_adding_page.fill_data_product_info(model=model)

    with allure.step(f'Сохранить продукт {product_name}'):
        admin_product_adding_page.submit_adding_product_button_click()

    with allure.step(f'Отфильтровать продукт {product_name}'):
        admin_products_page.filter_product_by_name(product_name)
        product_name_list = admin_products_page.product_names_get()
        filtered_product_name = product_name_list[0].text
    assert filtered_product_name == product_name


@allure.title('Удаление товара админом')
@allure.severity(severity_level=Severity.NORMAL)
def test_delete_product(browser, base_url):
    admin_login_page = AdminLoginPage(browser)
    admin_main_page = AdminMainPage(browser)
    admin_products_page = AdminProductsPage(browser)

    with allure.step('Логин под админом и переход в Каталог'):
        admin_login_page.login()
        admin_main_page.open_products_catalog()

    previous_products_count = admin_products_page.products_count_get()

    with allure.step('Удаление последнего продукта в списке'):
        admin_products_page.last_checkbox_in_list_click()
        admin_products_page.delete_button_click()
        browser.switch_to.alert.accept()

    current_products_count = admin_products_page.products_count_get()

    assert previous_products_count - current_products_count == 1


@allure.title('Проверка количества пользователей на сайте')
@allure.severity(severity_level=Severity.NORMAL)
def test_check_customers_count(browser, base_url, db_connector):
    admin_login_page = AdminLoginPage(browser)
    admin_main_page = AdminMainPage(browser)
    actual_customer_count = db_connector.get_customers_count()

    with allure.step('Логин под админом'):
        admin_login_page.login()

    with allure.step('Проверка отображаемого количества пользователей'):
        customer_count = admin_main_page.get_customers_count()
        assert customer_count == actual_customer_count


@allure.title('Проверка количества заказов на сайте')
@allure.severity(severity_level=Severity.NORMAL)
def test_check_orders_count(browser, base_url, db_connector):
    admin_login_page = AdminLoginPage(browser)
    admin_main_page = AdminMainPage(browser)
    actual_customer_count = db_connector.get_active_orders_count()

    with allure.step('Логин под админом'):
        admin_login_page.login()

    with allure.step('Проверка отображаемого количества заказов'):
        customer_count = admin_main_page.get_orders_count()
        assert customer_count == actual_customer_count
