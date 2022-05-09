import os
import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.opera import options as OperaOptions

DRIVERS = "~/Downloads/drivers"


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/drivers"))
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", default="http://192.168.1.6:8081/")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")
    if browser == 'chrome':
        options = ChromeOptions()
        if headless:
            options.headless = True
        # можно ли использовать этот вариант, чтобы не вылезали ворнинги?
        # https://pypi.org/project/webdriver-manager/3.5.4/
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver = webdriver.Chrome(executable_path=f'{drivers}/chromedriver', options=options)
    elif browser == 'firefox':
        options = FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(executable_path=f'{drivers}/geckodriver', options=options)
    elif browser == 'opera':
        opera_options = OperaOptions.ChromeOptions()
        if headless:
            opera_options.headless = True
        driver = webdriver.Opera(executable_path=f'{drivers}/operadriver', options=opera_options)
    else:
        raise ValueError("Driver is not supported")

    driver.maximize_window()
    request.addfinalizer(driver.close)
    return driver


@pytest.fixture()
def base_url(request):
    return request.config.getoption('--url')
