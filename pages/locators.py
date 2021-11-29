from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_PRODUCT_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MAIN_NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    NAME_OF_PRODUCT_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    MAIN_PRICE_OF_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    PRICE_OF_PRODUCT_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")
