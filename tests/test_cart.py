"""
购物车模块测试用例
"""
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestCart:
    """购物车测试类"""

    @pytest.fixture(autouse=True)
    def login_and_add_item(self, driver):
        """每个用例执行前：登录 + 加1个商品到购物车"""
        login_page = LoginPage(driver)
        login_page.open_page()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.add_first_product_to_cart()
        return driver

    def test_cart_has_one_item(self, driver):
        """用例1：购物车中有1个商品"""
        inventory_page = InventoryPage(driver)
        inventory_page.go_to_cart()

        cart_page = CartPage(driver)
        assert cart_page.get_item_count() == 1
        print("[OK] 购物车中有1个商品")

    def test_cart_item_name_correct(self, driver):
        """用例2：购物车中商品名称正确"""
        inventory_page = InventoryPage(driver)
        names_before = inventory_page.get_product_names()
        first_name_before = names_before[0]

        inventory_page.go_to_cart()
        cart_page = CartPage(driver)
        names_in_cart = cart_page.get_item_names()

        assert first_name_before in names_in_cart
        print(f"[OK] 购物车商品名称正确：{first_name_before}")

    def test_remove_item_from_cart(self, driver):
        """用例3：从购物车移除商品"""
        inventory_page = InventoryPage(driver)
        inventory_page.go_to_cart()

        cart_page = CartPage(driver)
        assert cart_page.get_item_count() == 1
        cart_page.remove_first_item()
        assert cart_page.get_item_count() == 0
        print("[OK] 商品移除成功")

    def test_continue_shopping(self, driver):
        """用例4：继续购物按钮返回商品列表"""
        inventory_page = InventoryPage(driver)
        inventory_page.go_to_cart()

        cart_page = CartPage(driver)
        cart_page.click_continue_shopping()

        assert "inventory" in driver.current_url
        print("[OK] 继续购物返回商品列表")

    def test_click_checkout(self, driver):
        """用例5：点击结算进入结算流程"""
        inventory_page = InventoryPage(driver)
        inventory_page.go_to_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        assert "checkout-step-one" in driver.current_url
        print("[OK] 进入结算流程")