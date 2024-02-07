from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser: WebDriver, url: str, timeout=10):
        super().__init__(browser, url, timeout)
