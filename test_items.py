import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import pytest

import os
import dotenv


dotenv.load_dotenv()
links_list = (
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
)

mail = os.getenv('EMAIL')
passw = os.getenv('PASSWORD')


@pytest.mark.items
def test_items(browser):
    browser.implicitly_wait(5)
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(url)
    message = 'Incorrect amount of buttons'
    buttons = browser.find_elements(
        By.CSS_SELECTOR, '.btn-add-to-basket'
        )
    assert len(buttons) == 1, message


@pytest.mark.pages
@pytest.mark.parametrize('url', (links_list))
def test_login(browser, url):
    browser.get(url)
    browser.implicitly_wait(5)
    browser.find_element(By.CSS_SELECTOR, '.navbar__auth_login').click()
    browser.find_element(
        By.CSS_SELECTOR, '[name=\'login\']'
        ).send_keys(mail)
    browser.find_element(
        By.CSS_SELECTOR, '[name=\'password\']'
        ).send_keys(passw)
    browser.find_element(By.CSS_SELECTOR, '.sign-form__btn').click()
    time.sleep(5)
    answer = math.log(int(time.time()))
    browser.find_element(
        By.CSS_SELECTOR, '.string-quiz__textarea'
        ).send_keys(answer)
    button = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
    WebDriverWait(browser, 5).until_not(
        EC.element_attribute_to_include((
            By.CSS_SELECTOR, '.submit-submission'), 'disabled'))
    button.click()
    answer = browser.find_element(
        By.CSS_SELECTOR, '.smart-hints__hint'
        ).text
    browser.find_element(By.CSS_SELECTOR, '.navbar__profile-toggler')
    browser.find_element(
        By.CSS_SELECTOR, '.attempt__actions > button.again-btn.white'
        ).click()
    assert answer == 'Correct!', 'Wrong answer!'
