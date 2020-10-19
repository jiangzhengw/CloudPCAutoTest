# Time: 2020/10/19 14:49
# Author: jiangzhw
# FileName: email.py
from selenium.webdriver.common.by import By

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
        assert self._driver.find_element(*email_title).text == "微邮"
        assert self._driver.find_element(*email_title2).text == "收件人"
        assert self._driver.find_element(*email_title3).text == "主题"
        assert self._driver.find_elements(*email_title2)[1].text == "正文"
        assert self._driver.find_element(*email_right_title).text == "添加收件人"
        assert self._driver.find_element(*email_right_all).text == "全选"
        self.is_element_exit(add_button)
        self.is_element_exit(clear_button)
        self.is_element_exit(search_button)
        self.is_element_exit(save_button)
        self.is_element_exit(send_button)

    def modify_topic(self):
        """微邮-修改标题"""
        pass

    def add_attachment(self):
        """微邮-添加附件"""
        pass

    def insert_content(self):
        """微邮-输入内容"""
        pass

    def clear_content(self):
        """微邮-清空按钮"""
        pass

    def search(self):
        """微邮-搜索"""
        pass

    def select_member(self):
        """微邮-选择成员"""
        pass

    def select_all(self):
        """微邮-选择全部成员"""
        pass

    def modify_content_style(self):
        """微邮-修改内容样式"""
        pass
