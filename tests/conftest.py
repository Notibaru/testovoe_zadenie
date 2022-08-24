import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def get_webdriwer():
    options = get_chrome_options
    driver = webdriver.Chrome()
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriwer):
    driver = get_webdriwer
    url = 'https://xn--d1abb2a.xn--p1ai/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.close()
