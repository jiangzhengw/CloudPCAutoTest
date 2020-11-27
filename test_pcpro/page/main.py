# Time: 2020/9/27 11:36
# Author: jiangzhw
# FileName: main.py
from time import sleep

import pytest
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
        return Login(self._driver)

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
        print("进入login_out 方法")
        sidebar_button = (By.CSS_SELECTOR, '.sidebar-button-container .sidebar-button img')
        out_button = (By.CSS_SELECTOR, '.more-popover-button .ic-left')
        self.wait(10, ec.element_to_be_clickable(sidebar_button))
        self.find(sidebar_button).click()
        self.wait(10, ec.element_to_be_clickable(out_button))
        self.find(out_button).click()

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
        assert "姜正炜" in self.find(user_name).text
        assert self.find(position).text == "员工"
        self.is_element_exit(avatar)
        assert self.find(tel).text == "17864199426"
        assert self.find(mail).text == "jiangzhw01@inspur.com"
        assert "爱城市网测试处" in self.find(connection).text
        # assert "浪潮集团" == self.find(group).text

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
        assert "组织绑定" == self.find(org_title).text
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
            self.find(name_input).send_keys(name)
            self.find(pwd_input).send_keys(pwd)
        if self.is_element_exit(tel_input):
            self.find(tel_input).send_keys(name)
            self.find(yzm_input).send_keys(pwd)

    def bind_group_operation(self):
        """组织绑定信息填写"""
        # Todo:方法优化，优化验证码和账号密码绑定逻辑
        bind_submit = (By.CSS_SELECTOR, 'button[class="cc-btn btn-bind cc-btn-default cc-btn-size-default"]')
        msg_toast = (By.CSS_SELECTOR, '.cc-message-box')
        msg_define = (By.CSS_SELECTOR, '.cc-message-box-btns .cc-btn-default')
        self.wait(10, ec.element_to_be_clickable(bind_submit))
        self.find(bind_submit).click()
        self.wait(10, ec.element_to_be_clickable(msg_toast))
        self.find(msg_define).click()
        self.wait(10, ec.invisibility_of_element(msg_toast))
        self.enter_bind_msg("17864199426", "123456a?")
        self.find(bind_submit).click()

    def person_info_operation(self):
        """个人信息操作"""
        self.person_avatar_hover()
        # 悬浮后打印page_source，便于定位
        # print(self._driver.page_source)
        self.assert_person_info()
        self.bind_group_click()
        self.assert_bind_group()

    # Todo:增加对模糊搜索场景的编写（同名增加部门校验处理）
    def precise_search(self, name):
        """首页搜索"""
        self.search(name)
        search = (By.CSS_SELECTOR, '.chat-list-search input[placeholder="搜索"]')
        self.mouse_hover(search)
        search_clear = (By.CSS_SELECTOR, '.ic-close-fill.cc-input__clear')
        self.wait(10, ec.element_to_be_clickable(search_clear))
        self.find(search_clear).click()
        self.wait_element_display(search_clear)
        pytest.assume(self.find(search).text == "")
        self.search(name)
        search_empty = (By.CSS_SELECTOR, '.chat-search-empty span')
        if self.is_element_exit(search_empty):
            self.wait(10, ec.presence_of_element_located(search_empty))
            pytest.assume(self.find(search_empty).text == "暂无匹配联系人")
        else:
            search_title = (By.CSS_SELECTOR, '.chat-search-title')
            self.wait(10, ec.visibility_of_element_located(search_title))
            search_title = (By.CSS_SELECTOR, '.chat-search-detail-title')
            search_en_title = (By.CSS_SELECTOR, '.chat-search-detail-title small')
            chat_title = (By.CSS_SELECTOR, f'span[title="{name}"]')
            self.wait(10, ec.visibility_of_element_located(search_title))
            if len(self._driver.find_elements(*search_title)) == 1:
                self.find(search_title).click()
            else:
                for i in range(len(self._driver.find_elements(*search_title))):
                    text = self._driver.find_elements(*search_title)[i].text
                    text_en = self._driver.find_elements(*search_en_title)[i].text
                    text = text.replace(text_en, "", 1)
                    text.strip()
                    print(text)
                    if name == text:
                        self._driver.find_elements(*search_title)[i].click()
                self.wait(10, ec.presence_of_element_located(chat_title))
