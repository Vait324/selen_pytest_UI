from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest


def test_guest_can_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.product
@pytest.mark.parametrize(
    'promo_number', [
        pytest.param(number, marks=pytest.mark.xfail(
            number == 7, reason='incorrect page')
                ) for number in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_number):
    link = ('http://selenium1py.pythonanywhere.com/catalogue/'
            f'coders-at-work_207/?promo=offer{promo_number}')
    page = ProductPage(browser, ''.join(link))
    page.open()
    page.should_be_product_page()
    page.add_product_to_basket()
