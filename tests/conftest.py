"""
pytest 配置文件
"""
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="function")
def driver():
    """浏览器 fixture"""
    print("\n[Fixture] 启动 Edge 浏览器...")
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    print("\n[Fixture] 关闭浏览器...")
    driver.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """已登录状态的 fixture"""
    from pages.login_page import LoginPage
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")
    return driver