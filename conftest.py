import datetime
import logging
import os
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.opera import options as OperaOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/drivers"))
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", default="http://192.168.0.13:8082/")
    parser.addoption("--log_level", default="DEBUG")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    logger.addHandler(logging.FileHandler(f"logs/{request.node.name}.log"))
    logger.setLevel(level=log_level)

    date_test_started = datetime.datetime.now()
    logger.info(f"===> Test {request.node.name} started at {date_test_started}")
    if browser == 'chrome':
        options = ChromeOptions()
        if headless:
            options.headless = True
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

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    def fin():
        driver.quit()
        date_test_finished = datetime.datetime.now()
        logger.info(
            f"===> Test {request.node.name} finished at {date_test_finished}. "
            f"It was completed for {date_test_finished - date_test_started}")

    request.addfinalizer(fin)

    def open_path(path=""):
        return driver.get(url + path)

    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.open = open_path
    driver.open()

    return driver


@pytest.fixture()
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture(autouse=True)
def change_test_dir(request, monkeypatch):
    monkeypatch.chdir(request.fspath.dirname)
