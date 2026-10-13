"""
购物车页面对象
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """购物车页面"""

    URL = "https://www.saucedemo.com/cart.html"

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='remove']")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def open_page(self):
        self.open(self.URL)
        return self

    def get_item_count(self):
        """购物车中商品数量"""
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def get_item_names(self):
        """购物车中所有商品名称"""
        elements = self.driver.find_elements(*self.ITEM_NAMES)
        return [e.text for e in elements]

    def remove_first_item(self):
        """移除第一个商品"""
        buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
        buttons[0].click()

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)