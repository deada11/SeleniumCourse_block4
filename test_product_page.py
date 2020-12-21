from .pages.product_page import ProductPage

product_page_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

@pytest.mark.parametrize()
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.product_name_correct()
    page.product_price_correct()
