from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_PRICE_LOCATOR = (By.CSS_SELECTOR, ".alertinner>p>strong")
    PRODUCT_PRICE_LOCATOR = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME_IN_BASKET_LOCATOR = (By.CSS_SELECTOR, ".alertinner>strong")
    PRODUCT_NAME_ON_PAGE_LOCATOR = (By.CSS_SELECTOR, ".product_main>h1")
