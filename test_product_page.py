from .pages.product_page import ProductPage
from .pages.base_page import URLs
import pytest

product_page_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
product_page_withot_promo_link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207'


@pytest.mark.skip
@pytest.mark.parametrize('product_page_links', URLs)
def test_guest_can_add_product_to_basket(browser, product_page_links):
    page = ProductPage(browser, product_page_links)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.product_name_correct()
    page.product_price_correct()

@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_page_withot_promo_link)
    page.open()
    page.add_product_to_basket()
    page.guest_cant_see_success_message_after_adding_product_to_basket()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_page_withot_promo_link)
    page.open()
    page.guest_cant_see_success_message()

@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_page_withot_promo_link)
    page.open()
    page.add_product_to_basket()
    page.message_disappeared_after_adding_product_to_basket()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_page_withot_promo_link)
    page.open()
    page.go_to_login_page()