# Time: 2020/11/11 9:42
# Author: jiangzhw
# FileName: login.py
import time

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
    _remember_button = (By.CSS_SELECTOR, '.login-remember .cc-checkbox-inner')
    _is_checked = (By.CSS_SELECTOR, '.login-remember .is-checked')

    def login_in_assert(self):
        """登录页面断言"""
        print("进入login_in_assert方法")
        self.wait(10, ec.visibility_of_element_located(self._login_container))
        assert self.find(self._welcome_img)
        assert self.find(self._change_group)
        assert self.find(self._input_name)
        assert self.find(self._input_pwd)
        assert self.find(self._forget_pwd).text == "记住密码"
        assert self.find(self._login_button)

    def toast_confirm_click(self, type):
        """点击toast确认按钮"""
        confirm_button = (By.CSS_SELECTOR, '.cc-message-box-btns button')
        back_button = (By.CSS_SELECTOR, '.org-bind-head .ic-arrow-left')
        if type == "login":
            if self.is_ele_clickable(confirm_button):
                self.find(confirm_button).click()
                time.sleep(1)
        elif type == "bind":
            if self.is_ele_clickable(confirm_button):
                self.find(confirm_button).click()
                self.wait(10, ec.element_to_be_clickable(back_button))
                self.find(back_button).click()
                self.wait(10, ec.visibility_of_element_located(self._login_button))
        else:
            self.wait(10, ec.visibility_of_element_located(self._login_button))

    def input_login_msg(self, name, pwd):
        """输入登录信息"""
        eye = (By.CSS_SELECTOR, '.cc-input__suffix-inner')
        self.wait(10, ec.element_to_be_clickable(self._input_name))
        time.sleep(0.5)
        self.mouse_hover(self._input_name)
        # print(self._driver.page_source)
        if self.is_element_exit(self._close_fill):
            self.wait(10, ec.element_to_be_clickable(self._close_fill))
            self.find(self._close_fill).click()
            self.mouse_hover(self._input_pwd)
            if self.is_element_exit(self._close_fill):
                self.find(eye).click()
                self.wait(10, ec.element_to_be_clickable(self._close_fill))
                self.find(self._close_fill).click()
        self.find(self._input_name).send_keys(name)
        self.find(self._input_pwd).send_keys(pwd)

    def remember_pwd(self, rescue=True):
        """记住/取消记住密码"""
        if rescue:
            if self.is_element_exit(self._is_checked):
                print("已记住密码")
            else:
                self.find(self._remember_button).click()
        else:
            if self.is_element_exit(self._is_checked):
                self.find(self._remember_button).click()
            else:
                print("已取消记住密码")

    def toast_assert(self, toast_text, type):
        """点击登录按钮toast断言"""
        toast = (By.CSS_SELECTOR, '.cc-message-box')
        toast_content = (By.CSS_SELECTOR, '.cc-message-box-message')
        self.wait(10, ec.visibility_of_element_located(toast))
        text = self.find(toast_content).text
        print(text)
        print(toast_text)
        if text is not None:
            pytest.assume(toast_text == text)
        else:
            self._logger.error("Toast Content is empty !")
        self.toast_confirm_click(type)

    def login_submit(self):
        """点击登录按钮"""
        self.find(self._login_button).click()

    def pwd_not_empty(self):
        """判断密码是否为空"""
        self.wait(10, ec.element_to_be_clickable(self._login_button))
        eye = (By.CSS_SELECTOR, '.cc-input__suffix-inner')
        return self.is_ele_clickable(eye)

    def change_group(self, group_code=None):
        """切换组织"""
        print("进入change_group方法")
        bind_button = (By.CSS_SELECTOR, 'span[class="btn-bind"]')
        input_group = (By.CSS_SELECTOR, 'input[placeholder="请输入组织代号"]')
        self.find(self._change_group).click()
        self.wait(10, ec.visibility_of_element_located(bind_button))
        self.find(input_group).send_keys(group_code)
        self.find(bind_button).click()
        time.sleep(1)

    def clear_bind_group(self):
        """清空绑定组织"""
        history_group = (By.CSS_SELECTOR, '.history-item')
        bind_button = (By.CSS_SELECTOR, 'span[class="btn-bind"]')
        active_bind = (By.CSS_SELECTOR, '[class="history-item active"]')
        cancel_bind = (By.CSS_SELECTOR, '[title="解绑"]')
        del_bind = (By.CSS_SELECTOR, '[title="删除"]')
        change_bind = (By.CSS_SELECTOR, '[title="切换"]')
        back_button = (By.CSS_SELECTOR, '.org-bind-head .ic-arrow-left')
        self.find(self._change_group).click()
        self.wait(10, ec.visibility_of_element_located(bind_button))
        # 解绑当前组织
        if self.is_element_exit(active_bind):
            self.mouse_hover(active_bind)
            self.wait(10, ec.element_to_be_clickable(cancel_bind))
            self.find(cancel_bind).click()
            self.wait(10, ec.visibility_of_element_located((By.CSS_SELECTOR, '.cc-message-box')))
            self.find((By.LINK_TEXT, "确定")).click()
        # 删除历史组织
        self.wait(10, ec.visibility_of_element_located(bind_button))
        len_history_group = len(self._driver.find_elements(*history_group))
        # print(len_history_group)
        if len_history_group > 0:
            for i in range(len_history_group):
                self.wait(10, ec.element_to_be_clickable(history_group))
                self.mouse_hover(history_group)
                self.wait(10, ec.element_to_be_clickable(del_bind))
                self.find(del_bind).click()
        self.find(back_button).click()
        self.wait(10, ec.visibility_of_element_located(self._login_container))

    def forget_pwd(self, phone, yzm, pwd, toast_content):
        """登录-忘记密码 验证码"""
        get_yzm = (By.CSS_SELECTOR, '.cc-input-group__append .cc-btn')
        forget_pwd = (By.CSS_SELECTOR, '.login-forget')
        self.find(forget_pwd).click()
        self.wait(10, ec.presence_of_element_located(get_yzm))
        phone_input = (By.CSS_SELECTOR, '.pwd-forgot-input input[placeholder="请输入手机号"]')
        yzm_input = (By.CSS_SELECTOR, '.pwd-forgot-input input[placeholder="请输入验证码"]')
        pwd_input = (By.CSS_SELECTOR, '.pwd-forgot-input input[placeholder="请输入新密码"]')
        save_button = (By.CSS_SELECTOR, '.cc-btn.login-btn')
        self.find(phone_input).send_keys(phone)
        # self.find(get_yzm).click()
        # self.toast_assert("forget_yzm", toast_content)
        self.find(yzm_input).send_keys(yzm)
        self.find(pwd_input).send_keys(pwd)
        self.find(save_button).click()
        self.toast_assert(toast_content, "bind")

    # Todo: forget_pwd_yzm() 和 login_yzm（）方法实现
    def forget_pwd_yzm(self):
        """忘记密码-获取验证码"""
        pass

    def login_yzm(self):
        """互联网环境-验证码登录"""
        pass
