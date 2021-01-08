from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time


product_page_without_promo_link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207'
product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.guest_tests
class TestGuestDoSomethingOnSite():

    @pytest.mark.need_review
    @pytest.mark.parametrize('promo_offer', ["?promo=offer0", "?promo=offer1",
                                             "?promo=offer2", "?promo=offer3",
                                             "?promo=offer4", "?promo=offer5",
                                             "?promo=offer6",
                                             pytest.param("?promo=offer7", marks=pytest.mark.xfail()),
                                             "?promo=offer8", "?promo=offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        link = product_link + promo_offer
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.product_name_correct()
        page.product_price_correct()


    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, product_page_without_promo_link)
        page.open()
        page.add_product_to_basket()
        page.guest_cant_see_success_message_after_adding_product_to_basket()


    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_page_without_promo_link)
        page.open()
        page.guest_cant_see_success_message()


    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, product_page_without_promo_link)
        page.open()
        page.add_product_to_basket()
        page.message_disappeared_after_adding_product_to_basket()


    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()


    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, product_page_without_promo_link)
        page.open()
        page.go_to_login_page()


    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, product_page_without_promo_link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.guest_cant_see_product_in_basket_opened_from_main_page()
        basket_page.guest_can_see_text_about_empty_basket_opened_from_main_page()


@pytest.mark.user_tests
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        register_link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        login_page = LoginPage(browser, register_link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "test-password"
        login_page.register_new_user(email=email, password=password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.guest_cant_see_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_basket()
        page.product_name_correct()
        page.product_price_correct()
