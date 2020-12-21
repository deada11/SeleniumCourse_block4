from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators():
    PRODUCT_FORM = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    PRODUCT_MESSAGE_NAME = (By.CSS_SELECTOR, '#messages >.alert:first-child > .alertinner > strong')
    PRODUCT_MESSAGE_PRICE = (By.CSS_SELECTOR, '#messages >.alert:last-child > .alertinner > p:first-child > strong')
