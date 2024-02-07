from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time

MAIN_LINK = ('http://selenium1py.pythonanywhere.com/en-gb/catalogue/'
             'the-city-and-the-stars_95/')
REG_LINK = ('http://selenium1py.pythonanywhere.com/en-gb/accounts/login/')
EMAIL = str(time.time()) + "@fakemail.org"
PASSWORD = '12345678999'


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, ''.join(REG_LINK))
        page.open()
        page.should_be_login_page()
        page.register_new_user(EMAIL, PASSWORD)
        page.should_be_authorized_user()

    @pytest.mark.parametrize(
        'promo_number', [
            pytest.param(number, marks=pytest.mark.xfail(
                number == 7, reason='incorrect page')
                # Temporary little number of pages. Should be > 7.
                    ) for number in range(1)])
    def test_user_can_add_product_to_basket(self, browser, promo_number):
        link = ('http://selenium1py.pythonanywhere.com/catalogue/'
                f'coders-at-work_207/?promo=offer{promo_number}')
        page = ProductPage(browser, ''.join(link))
        page.open()
        page.should_be_product_page()
        page.should_not_be_success_message()
        page.add_product_to_basket()


@pytest.mark.need_review
class TestLoginOnProductPage:
    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, ''.join(MAIN_LINK))
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, ''.join(MAIN_LINK))
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


@pytest.mark.need_review
class TestGuestProduct:
    def test_guest_cant_see_product_in_basket_opened(self, browser):
        page = ProductPage(browser, ''.join(MAIN_LINK))
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page()
        basket_page.should_be_empty_basket()

    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, ''.join(MAIN_LINK))
        page.open()
        page.should_be_product_page()
        page.should_not_be_success_message()
        page.add_product_to_basket()
