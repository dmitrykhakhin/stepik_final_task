from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.pres_add_to_basket()
    page.solve_quiz_and_get_code()
#    time.sleep(500)
    page.name_of_product_is_equal()
    page.price_is_equal()
