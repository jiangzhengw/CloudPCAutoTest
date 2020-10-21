# Time: 2020/10/21 14:35
# Author: jiangzhw
# FileName: notice.py
from selenium.webdriver.common.by import By

from test_pcpro.page.base_page import BasePage


class Notice(BasePage):
    """通知公告 Page"""

    def assert_notice(self):
        """通知公告页面断言"""
        title = (By.CSS_SELECTOR, '.chat-detail-container .chat-detail-title-bar')
        notice_list = (By.CSS_SELECTOR, '.chat-notice-list-item-center')
        assert self._driver.find_element(*title).text == "通知公告"
        self.is_element_exit(notice_list)
