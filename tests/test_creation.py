import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from pom.page import Page


@pytest.mark.usefixtures('setup')
class TestCreation:

    def test_page(self):
        page_link = Page(self.driver)
