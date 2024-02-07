from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        value = 'Basket'
        answer, _ = self.is_element_present(
            *BasketPageLocators.BASKET_HEADER, value
            )
        assert answer == value, f'Should be {value}, but {answer}'

    def should_be_empty_basket(self):
        value = 'Your basket is empty. Continue shopping'
        self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)
        answer, _ = self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_VALUE, value
            )
        assert answer == value, f'Should be {value}, but {answer}'
