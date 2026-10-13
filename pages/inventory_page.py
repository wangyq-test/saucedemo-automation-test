"""
商品列表页面对象
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """商品列表页"""

    URL = "https://www.saucedemo.com/inventory.html"

    # 排序下拉框
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    # 所有商品名称
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    # 所有商品价格
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    # 所有"加入购物车"按钮
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
    # 购物车角标
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    # 购物车图标
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def open_page(self):
        self.open(self.URL)
        return self

    def get_product_names(self):
        """获取所有商品名称列表"""
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [e.text for e in elements]

    def get_product_prices(self):
        """获取所有商品价格列表（转成数字）"""
        elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        return [float(e.text.replace("$", "")) for e in elements]

    def select_sort(self, value):
        """
        选择排序方式
        value 可选：
          'az'  - Name (A to Z)
          'za'  - Name (Z to A)
          'lohi' - Price (low to high)
          'hilo' - Price (high to low)
        """
        select = Select(self.driver.find_element(*self.SORT_DROPDOWN))
        select.select_by_value(value)

    def add_first_product_to_cart(self):
        """把第一个商品加入购物车"""
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        buttons[0].click()

    def get_cart_badge_count(self):
        """获取购物车角标数字"""
        try:
            return int(self.driver.find_element(*self.CART_BADGE).text)
        except Exception:
            return 0

    def go_to_cart(self):
        """点击购物车图标"""
        self.click(self.CART_LINK)