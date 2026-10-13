"""
结算模块测试用例
"""
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestCheckout:
    """结算测试类"""

    @pytest.fixture(autouse=True)
    def prepare_checkout(self, driver):
        """每个用例执行前：登录 → 加商品 → 进购物车 → 点结算"""
        login_page = LoginPage(driver)
        login_page.open_page()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.add_first_product_to_cart()
        inventory_page.go_to_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        return driver

    def test_normal_checkout(self, driver):
        """用例1：正常结算流程"""
        page = CheckoutPage(driver)
        page.fill_info("Zhang", "San", "410000")
        page.click_continue()
        page.click_finish()

        assert "Thank you for your order" in page.get_complete_text()
        print("[OK] 订单完成")

    def test_empty_first_name(self, driver):
        """用例2：名字为空时提示"""
        page = CheckoutPage(driver)
        page.fill_info("", "San", "410000")
        page.click_continue()

        error = page.get_error_message()
        assert "First Name is required" in error
        print(f"[OK] 空名字提示正确：{error}")

    def test_empty_last_name(self, driver):
        """用例3：姓为空时提示"""
        page = CheckoutPage(driver)
        page.fill_info("Zhang", "", "410000")
        page.click_continue()

        error = page.get_error_message()
        assert "Last Name is required" in error
        print(f"[OK] 空姓提示正确：{error}")

    def test_empty_postal_code(self, driver):
        """用例4：邮编为空时提示"""
        page = CheckoutPage(driver)
        page.fill_info("Zhang", "San", "")
        page.click_continue()

        error = page.get_error_message()
        assert "Postal Code is required" in error
        print(f"[OK] 空邮编提示正确：{error}")

    def test_cancel_checkout(self, driver):
        """用例5：取消结算返回购物车"""
        page = CheckoutPage(driver)
        page.click_cancel()

        assert "cart" in driver.current_url
        print("[OK] 取消结算返回购物车")