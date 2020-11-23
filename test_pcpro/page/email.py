# Time: 2020/10/19 14:49
# Author: jiangzhw
# FileName: email.py
from time import sleep

import win32api
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from test_pcpro.page.base_page import BasePage


class EMAIL(BasePage):
    """EMAIL page"""

    def email_assert(self):
        """微邮首页断言"""
        print("进入微邮页面！")
        email_title = (By.CSS_SELECTOR, '.header span')
        email_title2 = (By.CSS_SELECTOR, '.first-line span[class="title-two"]')
        email_title3 = (By.CSS_SELECTOR, '.first-line.title-two')
        add_button = (By.CSS_SELECTOR, 'span[class="title-three button"]')
        clear_button = (By.CSS_SELECTOR, 'span[class="float button"]')
        email_right_title = (By.CSS_SELECTOR, '.write-right-container .right-header span[class="title"]')
        email_right_all = (By.CSS_SELECTOR, '.write-right-container .right-header span[class="right-text"]')
        search_button = (By.CSS_SELECTOR, '.group-member-search input')
        save_button = (By.CSS_SELECTOR, '.footer .cc-btn-plain-default')
        send_button = (By.CSS_SELECTOR, '.footer .cc-btn-primary')
        assert self.find(email_title).text == "微邮"
        assert self.find(email_title2).text == "收件人"
        assert self.find(email_title3).text == "主题"
        assert self._driver.find_elements(*email_title2)[1].text == "正文"
        assert self.find(email_right_title).text == "添加收件人"
        assert self.find(email_right_all).text == "全选"
        self.is_element_exit(add_button)
        self.is_element_exit(clear_button)
        self.is_element_exit(search_button)
        self.is_element_exit(save_button)
        self.is_element_exit(send_button)

    def modify_topic(self, topic):
        """微邮-修改标题"""
        # print("微邮-修改标题")
        input_modify = (By.CSS_SELECTOR, '.title-two + .cc-input--mini input')
        self.find(input_modify).clear()
        self.find(input_modify).send_keys(topic)
        return self.find(input_modify).text

    def add_attachment(self, attachment=None):
        """微邮-添加附件"""
        # print("微邮-添加附件")
        toast = (By.CSS_SELECTOR, '.cc-message-box')
        add_button = (By.CSS_SELECTOR, 'span[class="title-three button"]')
        self.find(add_button).click()
        sleep(3)
        win32api.keybd_event(27, 0, 0, 0)
        self.wait(10, ec.element_to_be_clickable(toast))
        self.is_element_exit(toast)
        win32api.keybd_event(13, 0, 0, 0)

    def insert_content(self, msg):
        """微邮-输入内容"""
        wait_ele = (By.CSS_SELECTOR, '.first-line span[class="title-two"]')
        self.wait(10, ec.element_to_be_clickable(wait_ele))
        self._driver.switch_to_frame("tinymce_ifr")
        content = (By.CSS_SELECTOR, '.mce-content-body p')
        self.find(content).send_keys(msg)

    def clear_member(self):
        """微邮-清空收件人按钮"""
        clear_button = (By.CSS_SELECTOR, 'span[class="float button"]')
        self.find(clear_button).click()

    def search(self, keyword):
        """微邮-搜索"""
        search_button = (By.CSS_SELECTOR, '.group-member-search input')
        self.find(search_button).send_keys(keyword)

    def select_member(self):
        """微邮-选中/取消选择成员"""
        selected = (By.CSS_SELECTOR, '.group-member-list-container .cc-checkbox-inner')
        if self.is_element_exit(selected):
            self.find(selected).click()

    def select_all(self):
        """微邮-选择/取消选择全部成员"""
        select_all = (By.CSS_SELECTOR, '.right-header .cc-checkbox-inner')
        if self.is_element_exit(select_all):
            self.find(select_all).click()

    def modify_content_style(self, B=False, i=False, U=False, S=False, uList=False, oList=False, Size=None):
        """微邮-修改内容样式
        :param B:加粗
        :param i:斜体
        :param U:下划线
        :param S:删除线
        :param uList:无序列表
        :param oList:有序列表
        :param Size:字体大小
        """
        self._driver.switch_to_default_content()
        sleep(1)
        ele_b = (By.CSS_SELECTOR, 'button[title="粗体"]')
        ele_i = (By.CSS_SELECTOR, 'button[title="斜体"]')
        ele_u = (By.CSS_SELECTOR, 'button[title="下划线"]')
        ele_s = (By.CSS_SELECTOR, 'button[title="删除线"]')
        ele_ul = (By.CSS_SELECTOR, 'button[title="项目符号"]')
        ele_ol = (By.CSS_SELECTOR, 'button[title="编号列表"]')
        ele_size = (By.CSS_SELECTOR, 'button[title="字号"]')
        font_menu = (By.CSS_SELECTOR, 'div[role="menu"]')

        if B:
            self.find(ele_b).click()
        if i:
            self.find(ele_i).click()
        if U:
            self.find(ele_u).click()
        if S:
            self.find(ele_s).click()
        if uList:
            self.find(ele_ul).click()
        if oList:
            self.find(ele_ol).click()
        if Size is not None:
            Size = str(Size) + "pt"
            self.find(ele_size).click()
            self.wait(10, ec.element_to_be_clickable(font_menu))
            length = len(self._driver.find_elements(By.CSS_SELECTOR, '.tox-collection__item-label'))
            for i in range(length):
                if self._driver.find_elements(By.CSS_SELECTOR, '.tox-collection__item-label')[i].text == Size:
                    self._driver.find_elements(By.CSS_SELECTOR, '.tox-collection__item-label')[i].click()

    def save(self):
        """微邮-保存"""
        save_button = (By.CSS_SELECTOR, '.footer .cc-btn-plain-default')
        self.find(save_button).click()

    def submit(self):
        """微邮-发送"""
        send_button = (By.CSS_SELECTOR, '.footer .cc-btn-primary')
        self.find(send_button).click()

    def close(self):
        """关闭微邮page"""
        close_button = (By.CSS_SELECTOR, '.btn-close')
        self.find(close_button).click()
