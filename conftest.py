import datetime
import json
import logging
import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.opera import options as OperaOptions

from db.db_requests import DbConnector


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/drivers"))
    parser.addoption("--headless", action="store_true")
    parser.addoption("--log_level", default="DEBUG")
    parser.addoption("--executor", default="http://192.168.0.12")
    parser.addoption("--url", default="http://192.168.0.12:8082")
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--videos", action="store_true")
    parser.addoption("--bv")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")
    url = request.config.getoption("--url")

    logger = logging.getLogger(request.node.name)
    if 'logs' not in os.listdir():
        os.mkdir('logs')
    logger.addHandler(logging.FileHandler(f"logs/{request.node.name}.log"))
    logger.setLevel(level=log_level)

    date_test_started = datetime.datetime.now()
    logger.info(f"===> Test {request.node.name} started at {date_test_started}")

    if executor == 'local':
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

    else:
        executor_url = f"{executor}:4444/wd/hub"

        caps = {
            "browserName": browser,
            "browserVersion": version,
            "name": "Elizaveta",
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs,
                "sessionTimeout": "2m"
            },
            'acceptSslCerts': True,
            'acceptInsecureCerts': True,
            'timeZone': 'Europe/Moscow',
            'goog:chromeOptions': {}
        }

        options = Options()

        if browser == 'opera':
            options.add_experimental_option('w3c', True)

        driver = webdriver.Remote(command_executor=executor_url,
                                  desired_capabilities=caps,
                                  options=options)

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    allure.attach(name=driver.session_id,
                  body=json.dumps(driver.capabilities),
                  attachment_type=allure.attachment_type.JSON)

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


@pytest.fixture(scope='session')
def db_connector(request):
    with open('target.json') as db_conf:
        db_config = json.load(db_conf)
    # data = request.config.getoption("--target")['db_connect']
    db_fixture = DbConnector(
        user=db_config['db_connect']['login'],
        password=db_config['db_connect']['password'],
        host=db_config['db_connect']['host'],
        port=db_config['db_connect']['port'],
        database=db_config['db_connect']['dbname']
    )

    def fin():
        db_fixture.destroy()

    request.addfinalizer(fin)
    return db_fixture


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.failed and rep.when == 'call':
        mode_for_failures = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode=mode_for_failures) as failure:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    failure.write('Fail to take screenshot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='fail_screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            failure.write('Fail to take screenshot: {}'.format(e))
