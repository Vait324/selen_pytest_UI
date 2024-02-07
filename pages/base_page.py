from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (NoAlertPresentException,
                                        TimeoutException)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

from .locators import BasePageLocators
import math


class BasePage:
    def __init__(self, browser: WebDriver, url: str, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Open an url by 'Webdriver.get()' method."""
        self.browser.get(self.url)

    def should_be_login_link(self):
        """Checking for a login link."""
        answer, error = self.is_element_present(*BasePageLocators.LOGIN_LINK)
        assert answer, \
            f'No login link on the page. Error is {error}'

    def go_to_login_page(self):
        """Find and click a login button."""
        login_link = self.browser.find_element(
            *BasePageLocators.LOGIN_LINK
        )
        login_link.click()

    def should_be_authorized_user(self):
        answer, error = self.is_element_present(
            *BasePageLocators.USER_ICON
            )
        message = f'User icon is not presented. Error is: {error}.'
        assert answer, message

    def go_to_basket_page(self):
        """Find and click a basket button."""
        basket_link = self.browser.find_element(
            *BasePageLocators.BASKET_LINK
        )
        basket_link.click()

    def is_element_present(self, how: str, what: str, value: str = ''
                           ) -> tuple[bool | str | property, Exception | None]:
        """
        Accepts arguments like 'WebDriver.find_element()' method. Returns a
        tuple with a boolean type answer and an Exception instance.
        If value argument is specidied then there will be comparsion
        with the text of the element.
        """
        element = WebElement
        answer = True
        error = None
        try:
            element = self.browser.find_element(how, what)
        except Exception as exc:
            answer = False
            error = exc
        if value:
            answer = element.text
        return answer, error

    def is_not_element_present(self, how: str, what: str, timeout=4
                               ) -> tuple[bool, str | None | Exception]:
        """
        Checking for element that should NOT be present.
        Accepts arguments like for the Expected_conditions"""
        answer = False
        error = f'Element {what} is present but should not.'
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((
                    how, what))
                )
        except TimeoutException:
            answer = True
            error = None
        except Exception as exc:
            answer = False
            error = exc
        return answer, error

    def solve_quiz_and_get_code(self):
        """Solving a quiz from pop-up alert."""
        try:
            alert = self.browser.switch_to.alert
            x = alert.text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
