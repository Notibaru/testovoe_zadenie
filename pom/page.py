from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement


class Page(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav_field: str = 'body > div.root-wrap.main-page > header > div > div > div.header_auth > div.header_auth-box > nav > a:nth-child(2)'

    def get_nav_field(self) -> WebElement:
        return self.is_visible('css', self.nav_field, 'auth field')
