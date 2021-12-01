from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def product_in_basket_is_not_presented(self):
        assert self.is_not_element_present(*BasePageLocators.PRODUCTS_IN_BASKET), \
            "Product in basket is presented, but should not be"

    def text_basket_is_empty_is_presented(self):
        text_basket_is_empty = self.browser.find_element(*BasePageLocators.TEXT_BASKET_IS_EMPTY)
        text_basket_is_empty_is_presented = text_basket_is_empty.text
        assert "Ваша корзина пуста" in text_basket_is_empty_is_presented, \
            "Text basket is empty is not presented, but should be"
