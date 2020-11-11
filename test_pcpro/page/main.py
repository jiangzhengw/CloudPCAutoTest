# Time: 2020/9/27 11:36
# Author: jiangzhw
# FileName: main.py
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from test_pcpro.page.base_page import BasePage
from test_pcpro.page.fwh import FWH
from test_pcpro.page.login import Login
from test_pcpro.page.notice import Notice


class Main(BasePage):
    """Main page"""

    def fwh_click(self):
        """点击打开服务号Page"""
        ele_fwh = (By.CSS_SELECTOR, ".chat-title")
        self.wait(10, ec.element_to_be_clickable(ele_fwh))
        sleep(3)
        ele_list = self._driver.find_elements(*ele_fwh)
        if len(ele_list) > 0:
            for i in range(len(ele_list)):
                if self._driver.find_elements(*ele_fwh)[i].text == "服务号":
                    # print(self._driver.find_elements(*ele_fwh)[i].text)
                    self._driver.find_elements(*ele_fwh)[i].click()
        else:
            raise NoSuchElementException()
        return FWH(self._driver)

    def enter_login_page(self):
        """切换到login page"""
        login_container = (By.CSS_SELECTOR, '.login-container')
        self.wait(10, ec.visibility_of_element_located(login_container))
        return Login()

    def notice_click(self):
        """点击打开通知公告page"""
        ele_notice = (By.CSS_SELECTOR, ".chat-title")
        self.wait(10, ec.element_to_be_clickable(ele_notice))
        sleep(3)
        ele_list = self._driver.find_elements(*ele_notice)
        if len(ele_list) > 0:
            for i in range(len(ele_list)):
                if self._driver.find_elements(*ele_notice)[i].text == "通知公告":
                    self._driver.find_elements(*ele_notice)[i].click()
        else:
            raise NoSuchElementException()
        return Notice(self._driver)

    def login_out(self):
        """login out"""
        ele_avatar = (By.CSS_SELECTOR, ".user-avatar img")
        self.wait(10, ec.element_to_be_clickable(ele_avatar))
        self.mouse_hover(ele_avatar)
        self._driver.find_element(By.LINK_TEXT, "登出").click()

    def person_avatar_hover(self):
        """个人头像-悬浮"""
        ele_avatar = (By.CSS_SELECTOR, ".user-avatar img")
        self.wait(10, ec.element_to_be_clickable(ele_avatar))
        self.mouse_hover(ele_avatar)

    def assert_person_info(self):
        """个人信息-断言"""
        user_name = (By.CSS_SELECTOR, '.user-popover-top .user-name')
        position = (By.CSS_SELECTOR, '.user-popover-top .user-name small')
        avatar = (By.CSS_SELECTOR, '.user-popover-avatar img')
        tel = (By.XPATH, '//*[@class="ic ic-telephone"]/..')
        mail = (By.XPATH, '//*[@class="ic ic-mail"]/..')
        connection = (By.XPATH, '//*[@class="ic ic-connections"]/..')
        # group = (By.CSS_SELECTOR, 'span[class="operate-name"]')

        self.wait(10, ec.element_to_be_clickable(user_name))
        print(self._driver.page_source)
        assert "姜正炜" in self._driver.find_element(*user_name).text
        assert self._driver.find_element(*position).text == "员工"
        self.is_element_exit(avatar)
        assert self._driver.find_element(*tel).text == "17864199426"
        assert self._driver.find_element(*mail).text == "jiangzhw01@inspur.com"
        assert "爱城市网测试处" in self._driver.find_element(*connection).text
        # assert "浪潮集团" == self._driver.find_element(*group).text

    def bind_group_click(self):
        """个人信息-组织绑定"""
        group = (By.CSS_SELECTOR, 'span[class="operate-name"]')
        banner = (By.CSS_SELECTOR, '.org-bind-pics')
        self._driver.find_elements(*group)[1].click()
        self.wait(10, ec.element_to_be_clickable(banner))
        # print(self._driver.page_source)

    def assert_bind_group(self):
        """绑定组织页面断言"""
        org_title = (By.XPATH, '//*[@class="cc-dialog-body"]/..//span[@class="org-bind-title"]')
        name_input = (By.CSS_SELECTOR, 'input[placeholder="互联网账号"]')
        pwd_input = (By.CSS_SELECTOR, 'input[placeholder="请输入密码"]')
        bind_submit = (By.CSS_SELECTOR, 'button[class="cc-btn btn-bind cc-btn-default cc-btn-size-default"]')
        yzm_login = (By.CSS_SELECTOR, '.org-internet-login-change')
        assert "组织绑定" == self._driver.find_element(*org_title).text
        self.is_element_exit(name_input)
        self.is_element_exit(pwd_input)
        self.is_element_exit(bind_submit)
        self.is_element_exit(yzm_login)

    def enter_bind_msg(self, name, pwd):
        """输入绑定信息"""
        name_input = (By.CSS_SELECTOR, 'input[placeholder="互联网账号"]')
        pwd_input = (By.CSS_SELECTOR, 'input[placeholder="请输入密码"]')
        tel_input = (By.CSS_SELECTOR, 'input[placeholder = "手机号"]')
        yzm_input = (By.CSS_SELECTOR, 'input[placeholder = "请输入验证码"]')
        if self.is_element_exit(name_input):
            self._driver.find_element(*name_input).send_keys(name)
            self._driver.find_element(*pwd_input).send_keys(pwd)
        if self.is_element_exit(tel_input):
            self._driver.find_element(*tel_input).send_keys(name)
            self._driver.find_element(*yzm_input).send_keys(pwd)

    def bind_group_operation(self):
        """组织绑定信息填写"""
        # Todo:方法优化，优化验证码和账号密码绑定逻辑
        bind_submit = (By.CSS_SELECTOR, 'button[class="cc-btn btn-bind cc-btn-default cc-btn-size-default"]')
        msg_toast = (By.CSS_SELECTOR, '.cc-message-box')
        msg_define = (By.CSS_SELECTOR, '.cc-message-box-btns .cc-btn-default')
        self.wait(10, ec.element_to_be_clickable(bind_submit))
        self._driver.find_element(*bind_submit).click()
        self.wait(10, ec.element_to_be_clickable(msg_toast))
        self._driver.find_element(*msg_define).click()
        self.wait(10, ec.invisibility_of_element(msg_toast))
        self.enter_bind_msg("17864199426", "123456a?")
        self._driver.find_element(*bind_submit).click()

    def person_info_operation(self):
        """个人信息操作"""
        self.person_avatar_hover()
        # 悬浮后打印page_source，便于定位
        # print(self._driver.page_source)
        self.assert_person_info()
        self.bind_group_click()
        self.assert_bind_group()
