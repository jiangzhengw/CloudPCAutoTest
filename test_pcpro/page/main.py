# Time: 2020/9/27 11:36
# Author: jiangzhw
# FileName: main.py
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from test_pcpro.page.base_page import BasePage
from test_pcpro.page.fwh import FWH
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
        """点击头像，个人信息断言"""
        user_name = (By.CSS_SELECTOR, '.user-popover-top .user-name')
        position = (By.CSS_SELECTOR, '.user-popover-top .user-name small')
        avatar = (By.CSS_SELECTOR, '.user-popover-avatar img')
        tel = (By.XPATH, '//*[@class="ic ic-telephone"]/..')
        mail = (By.XPATH, '//*[@class="ic ic-mail"]/..')
        connection = (By.XPATH, '//*[@class="ic ic-connections"]/..')

        self.wait(10, ec.element_to_be_clickable(user_name))
        assert "姜正炜" in self._driver.find_element(*user_name).text
        assert self._driver.find_element(*position).text == "员工"
        self.is_element_exit(avatar)
        assert self._driver.find_element(*tel).text == "17864199426"
        assert self._driver.find_element(*mail).text == "jiangzhw01@inspur.com"
        assert "爱城市网测试处" in self._driver.find_element(*connection).text

    def person_info_operation(self):
        """个人信息操作"""
        self.person_avatar_hover()
        # 悬浮后打印page_source，便于定位
        # print(self._driver.page_source)
        self.assert_person_info()
