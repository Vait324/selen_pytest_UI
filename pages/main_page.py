from .base_page import BasePage
# from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_login_link(self):
        answer, error = self.is_element_present(*MainPageLocators.LOGIN_LINK)
        assert answer, \
            f'No login link on the page. Error is {error}'

    def go_to_login_page(self):
        login_link = self.browser.find_element(
            *MainPageLocators.LOGIN_LINK
        )
        login_link.click()
