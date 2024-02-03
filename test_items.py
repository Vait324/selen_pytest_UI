from selenium.webdriver.common.by import By
import pytest


@pytest.mark.language
def test_language(browser):
    browser.implicitly_wait(5)
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(url)
    message = 'Incorrect amount of buttons'
    buttons = browser.find_elements(
        By.CSS_SELECTOR, '.btn-add-to-basket'
        )
    assert len(buttons) == 1, message
