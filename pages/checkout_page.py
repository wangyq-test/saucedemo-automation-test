"""
结算页面对象
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """结算页"""

    # 第一步：填写信息
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    # 第二步：确认订单
    FINISH_BUTTON = (By.ID, "finish")

    # 第三步：完成页
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def fill_info(self, first_name, last_name, postal_code):
        """填写收货信息"""
        self.input_text(self.FIRST_NAME_INPUT, first_name)
        self.input_text(self.LAST_NAME_INPUT, last_name)
        self.input_text(self.POSTAL_CODE_INPUT, postal_code)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def click_cancel(self):
        self.click(self.CANCEL_BUTTON)

    def click_finish(self):
        self.click(self.FINISH_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_complete_text(self):
        return self.get_text(self.COMPLETE_HEADER)

    def get_current_url(self):
        return self.driver.current_url