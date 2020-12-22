from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def guest_cant_see_product_in_basket_opened_from_main_page(self):
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), \
            "Basket is not empty, there are some products on it."

    def guest_can_see_text_about_empty_basket_opened_from_main_page(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "Basket is not empty! No text about it."
