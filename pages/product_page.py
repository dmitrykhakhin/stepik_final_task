from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import pytest


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_PRODUCT_TO_BASKET_BUTTON), "Button is not presented"

    def pres_add_to_basket(self):
        pres_button = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_TO_BASKET_BUTTON)
        pres_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def name_of_product_is_equal(self):
        main_name_of_product = self.browser.find_element(*ProductPageLocators.MAIN_NAME_OF_PRODUCT)
        main_name_of_product_text = main_name_of_product.text
        name_of_product_in_success_message = self.browser.find_element(
            *ProductPageLocators.NAME_OF_PRODUCT_IN_SUCCESS_MESSAGE)
        name_of_product_in_success_message_text = name_of_product_in_success_message.text
        assert main_name_of_product_text == name_of_product_in_success_message_text,\
            "Не совпадают названия продуктов!"

    def price_is_equal(self):
        main_price_of_product = self.browser.find_element(*ProductPageLocators.MAIN_PRICE_OF_PRODUCT)
        main_price_of_product_text = main_price_of_product.text
        price_of_product_in_success_message = self.browser.find_element(
            *ProductPageLocators.PRICE_OF_PRODUCT_IN_SUCCESS_MESSAGE)
        price_of_product_in_success_message_text = price_of_product_in_success_message.text
        assert main_price_of_product_text == price_of_product_in_success_message_text, "Цены не совпадают!"

    # def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
    #     assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
    #         "Success message is presented, but should not be"
    #
    # def test_guest_cant_see_success_message(self):
    #     assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
    #        "Success message is presented, but should not be"
    #
    # def test_message_disappeared_after_adding_product_to_basket(self):
    #     assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
    #         "Success message is presented, but should not be"
