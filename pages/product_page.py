from .base_page import BasePage
from .locators import ProductPageLocators, BasePageLocators


class ProductPage(BasePage):
    def click_on_basket_button(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def click_on_login_register_button(self):
        basket_button = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        basket_button.click()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is absent"

    def should_be_equal_price_on_page_and_basket(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert basket_price == product_price, f"Prices are not equal ({basket_price}!=({product_price}))"

    def should_be_equal_product_name_on_page_and_basket(self):
        basket_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PAGE).text
        assert basket_product_name == product_name, f"Names are not equal ({basket_product_name})!=({product_name}))"

    def should_not_be_success_message_on_present(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_on_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
