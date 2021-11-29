from .pages.product_page import ProductPage
from .pages.main_page import MainPage
import time
import pytest


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  #pytest.param(
                                  #    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo
                         #    =offer7"
                                  #    , marks=pytest.mark.xfail),
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
                                  ])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
#    page.test_guest_cant_see_success_message()
    page.should_be_add_to_basket_button()
    page.pres_add_to_basket()
    page.solve_quiz_and_get_code()
#    page.test_message_disappeared_after_adding_product_to_basket()
#    page.test_guest_cant_see_success_message_after_adding_product_to_basket()
#    time.sleep(100)
    page.name_of_product_is_equal()
    page.price_is_equal()
