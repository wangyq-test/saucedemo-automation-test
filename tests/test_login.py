"""
登录模块测试用例
"""
from pages.login_page import LoginPage


class TestLogin:
    """登录测试类"""

    def test_login_success(self, driver):
        """用例1：正确账号密码登录成功"""
        login_page = LoginPage(driver)
        login_page.open_page()
        login_page.login("standard_user", "secret_sauce")

        assert login_page.is_login_success(), "登录失败：未跳转到商品页"
        print("[OK] 登录成功测试通过")

    def test_login_wrong_password(self, driver):
        """用例2：错误密码登录失败"""
        login_page = LoginPage(driver)
        login_page.open_page()
        login_page.login("standard_user", "wrong_password")

        error_msg = login_page.get_error_message()
        assert "Username and password do not match" in error_msg
        print("[OK] 错误密码测试通过")

    def test_login_empty_username(self, driver):
        """用例3：用户名为空"""
        login_page = LoginPage(driver)
        login_page.open_page()
        login_page.login("", "secret_sauce")

        error_msg = login_page.get_error_message()
        assert "Username is required" in error_msg
        print("[OK] 空用户名测试通过")

    def test_login_empty_password(self, driver):
        """用例4：密码为空"""
        login_page = LoginPage(driver)
        login_page.open_page()
        login_page.login("standard_user", "")

        error_msg = login_page.get_error_message()
        assert "Password is required" in error_msg
        print("[OK] 空密码测试通过")

    def test_login_locked_user(self, driver):
        """用例5：锁定用户登录失败"""
        login_page = LoginPage(driver)
        login_page.open_page()
        login_page.login("locked_out_user", "secret_sauce")

        error_msg = login_page.get_error_message()
        assert "Sorry, this user has been locked out" in error_msg
        print("[OK] 锁定用户测试通过")