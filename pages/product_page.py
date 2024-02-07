from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def should_be_product_page(self):
        """Checking a page for matching with some product page."""
        self.should_be_reviews_block()
        self.should_be_product_descr()
        self.should_be_wishlist_button()

    def add_product_to_basket(self):
        """
        Adding some product to shopping basket and checking for matching
        to pop-up notification."""
        no_error = True
        message = None
        try:
            product_name = self.browser.find_element(
                *ProductPageLocators.PRODUCT_NAME
            ).text
            product_price = self.browser.find_element(
                *ProductPageLocators.PRODUCT_PRICE
            ).text
            self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET
                                      ).click()
            self.solve_quiz_and_get_code()
            notif_product_name = self.browser.find_element(
                *ProductPageLocators.NOTIF_PRODUCT_NAME
            ).text
            notif_product_price = self.browser.find_element(
                *ProductPageLocators.NOTIF_PRODUCT_PRICE
            ).text
            name_error = (
                f'Incorrect name of a product in notification.\
                Should be {product_name} but {notif_product_name}.'
                )
            price_error = (
                f'Incorrect price of a product in notification.\
                Should be {product_price} but {notif_product_price}.'
                )
            assert product_name == notif_product_name, name_error
            assert product_price == notif_product_price, price_error
        except Exception as exc:
            no_error = False
            message = f'Error is: {exc}'
        assert no_error, message

    def should_not_be_success_message(self):
        answer, error = self.is_not_element_present(
            *ProductPageLocators.NOTIF_PRODUCT_NAME)
        assert answer, error

    def should_be_product_descr(self):
        answer, error = self.is_element_present(
            *ProductPageLocators.PRODUCT_DESCRIPTION)
        assert answer, \
            f'No product description on the page. Error is {error}'

    def should_be_wishlist_button(self):
        answer, error = self.is_element_present(
            *ProductPageLocators.WISHLIST_BUTTON)
        assert answer, \
            f'No wishlist button on the page. Error is {error}'

    def should_be_reviews_block(self):
        answer, error = self.is_element_present(
            *ProductPageLocators.REVIEWS_BLOCK)
        assert answer, \
            f'No reviews block on the page. Error is {error}'
