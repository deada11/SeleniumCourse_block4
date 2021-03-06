from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group > a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p')
    NOT_EMPTY_BASKET = (By.CSS_SELECTOR, '.row > h2')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTER_EMAIL_FORM = (By.ID, 'id_registration-email')
    REGISTER_PASS_FORM = (By.ID, 'id_registration-password1')
    REGISTER_CONFIRM_PASS_FORM = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form > .btn')


class ProductPageLocators:
    PRODUCT_FORM = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    PRODUCT_MESSAGE_NAME = (By.CSS_SELECTOR, '#messages >.alert:first-child > .alertinner > strong')
    PRODUCT_MESSAGE_PRICE = (By.CSS_SELECTOR, '#messages >.alert:last-child > .alertinner > p:first-child > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages >.alert:first-child > .alertinner')
