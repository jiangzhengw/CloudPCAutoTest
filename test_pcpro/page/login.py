# Time: 2020/11/11 9:42
# Author: jiangzhw
# FileName: login.py
import pytest

from test_pcpro.page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class Login(BasePage):
    """login page"""
    _login_container = (By.CSS_SELECTOR, '.login-container')
    _welcome_img = (By.CSS_SELECTOR, '.login-head .welcome-img')
    _change_group = (By.CSS_SELECTOR, '.login-head button')
    _input_name = (By.CSS_SELECTOR, 'input[placeholder="请输入账号"]')
    _input_pwd = (By.CSS_SELECTOR, 'input[placeholder="请输入密码"]')
    _forget_pwd = (By.CSS_SELECTOR, '.login-remember-font')
    _login_button = (By.CSS_SELECTOR, '.login-btn')
    _close_fill = (By.CSS_SELECTOR, '.ic-close-fill')

    def login_in_assert(self):
        """登录页面断言"""
        self.wait(10, ec.visibility_of_element_located(self._login_container))
        assert self._driver.find_element(*self._welcome_img)
        assert self._driver.find_element(*self._change_group)
        assert self._driver.find_element(*self._input_name)
        assert self._driver.find_element(*self._input_pwd)
        assert self._driver.find_element(*self._forget_pwd).text == "记住密码"
        assert self._driver.find_element(*self._login_button)

    def clear_icon(self):
        """登录页面-清空已输入信息按钮"""
        self.mouse_hover(self._input_name)
        self.wait(10, ec.element_to_be_clickable(self._close_fill))
        # print(self._driver.page_source)
        self.mouse_hover(self._input_pwd)
        self.wait(10, ec.element_to_be_clickable(self._close_fill))

    @pytest.mark.parametrize('name,pwd', [
        ("test1", "12345"),
        ("test2", "123456"),
        ("test3", "哈哈哈哈"),
        ("test4", "*&*&^%%"),
        ("test5", "哈哈哈哈"),
        ("test6", "12345678901234567890123456789012345678901234567890")
    ])
    def input_login_msg(self, name, pwd):
        """输入登录信息"""
        self._driver.find_element(*self._input_name).send_keys(name)
        self._driver.find_element(*self._input_pwd).send_keys(pwd)
        self.login_submit()

    def login_submit(self):
        """点击登录按钮"""
        self._driver.find_element(*self._login_button).click()

    def bind_click(self):
        """点击绑定按钮"""
        bind_button = (By.CSS_SELECTOR, 'span[class="btn-bind"]')
        self._driver.find_element(*bind_button).click()

    @pytest.mark.parametrize("group_code", [
        "", "inspur", "INSPUR", "Inspur", "\000inspur", "inspur\000", "ins\000pur", "测试"
    ])
    def change_group_code(self, group_code):
        """切换组织"""
        self._driver.switch_to_window()
