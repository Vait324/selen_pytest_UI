from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, '#product_description')
    WISHLIST_BUTTON = (By.CSS_SELECTOR, '.btn, .btn-lg, .btn-wishlist')
    REVIEWS_BLOCK = (By.CSS_SELECTOR, '#reviews')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-primary, .btn-add-to-basket')
    NOTIF_PRODUCT_NAME = (
        By.CSS_SELECTOR, '#messages > div:nth-child(1) strong')
    NOTIF_PRODUCT_PRICE = (
        By.CSS_SELECTOR, '#messages > div:nth-child(3) strong')
