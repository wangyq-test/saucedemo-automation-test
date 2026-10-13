"""
商品列表模块测试用例
"""
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestInventory:
    """商品列表测试类"""

    @pytest.fixture(autouse=True)
    def login_first(self, driver):
        """每个用例执行前先登录"""
        login_page = LoginPage(driver)
        login_page.open_page()
        login_page.login("standard_user", "secret_sauce")
        return driver

    def test_product_count(self, driver):
        """用例1：商品列表显示6个商品"""
        page = InventoryPage(driver)
        names = page.get_product_names()
        assert len(names) == 6, f"期望6个商品，实际{len(names)}个"
        print(f"[OK] 商品数量正确，共{len(names)}个")

    def test_sort_price_low_to_high(self, driver):
        """用例2：价格从低到高排序"""
        page = InventoryPage(driver)
        page.select_sort("lohi")
        prices = page.get_product_prices()
        assert prices == sorted(prices), f"排序错误：{prices}"
        print(f"[OK] 价格升序正确：{prices}")

    def test_sort_price_high_to_low(self, driver):
        """用例3：价格从高到低排序"""
        page = InventoryPage(driver)
        page.select_sort("hilo")
        prices = page.get_product_prices()
        assert prices == sorted(prices, reverse=True), f"排序错误：{prices}"
        print(f"[OK] 价格降序正确：{prices}")

    def test_sort_name_a_to_z(self, driver):
        """用例4：名称A-Z排序"""
        page = InventoryPage(driver)
        page.select_sort("az")
        names = page.get_product_names()
        assert names == sorted(names), f"排序错误：{names}"
        print(f"[OK] 名称升序正确")

    def test_sort_name_z_to_a(self, driver):
        """用例5：名称Z-A排序"""
        page = InventoryPage(driver)
        page.select_sort("za")
        names = page.get_product_names()
        assert names == sorted(names, reverse=True), f"排序错误：{names}"
        print(f"[OK] 名称降序正确")

    def test_add_to_cart(self, driver):
        """用例6：添加商品到购物车，角标+1"""
        page = InventoryPage(driver)
        assert page.get_cart_badge_count() == 0
        page.add_first_product_to_cart()
        assert page.get_cart_badge_count() == 1
        print("[OK] 加入购物车后角标为1")