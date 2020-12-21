from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.PRODUCT_FORM).click()

    def product_name_correct(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_MESSAGE_NAME).text
        assert product_name in message_product_name, \
            f'Product name in message must be {product_name}, but {message_product_name}'

    def product_price_correct(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_MESSAGE_PRICE).text
        assert product_price in message_product_price, \
            f'Product price in basket must be {product_price}, but {message_product_price}'
