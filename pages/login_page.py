from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        """Checking a page for matching with a login page."""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email: str, password: str):
        no_error = True
        message = None
        try:
            self.browser.find_element(
                *LoginPageLocators.EMAIL_FIELD).send_keys(email)
            self.browser.find_element(
                *LoginPageLocators.PASSWORD_FIELD).send_keys(password)
            self.browser.find_element(
                *LoginPageLocators.PASSWORD_CONFIRM).send_keys(password)
            self.browser.find_element(
                *LoginPageLocators.REGISTER_BUTTON).click()
        except Exception as exc:
            no_error = False
            message = f'Exception is: {exc}'
        assert no_error, message

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, \
            'Not a login URL'

    def should_be_login_form(self):
        answer, error = self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert answer, \
            f'No login form on the page. Error is {error}'

    def should_be_register_form(self):
        answer, error = self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert answer, \
            f'No register form on the page. Error is {error}'
