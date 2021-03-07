from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_on_basket_button(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is absent"

    def should_be_equal_price_on_page_and_basket(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_LOCATOR).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_LOCATOR).text
        assert basket_price == product_price, f"Prices are not equal ({basket_price}!=({product_price}))"

    def should_be_equal_product_name_on_page_and_basket(self):
        basket_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET_LOCATOR).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PAGE_LOCATOR).text
        assert basket_product_name == product_name, f"Names are not equal ({basket_product_name})!=({product_name}))"
