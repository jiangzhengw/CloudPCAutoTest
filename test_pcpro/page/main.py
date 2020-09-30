# Time: 2020/9/27 11:36
# Author: jiangzhw
# FileName: main.py
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page.base_page import BasePage
from test_pcpro.page.fwh import FWH


class Main(BasePage):
    """Main page"""

    def fwh_click(self, timeout):
        """点击打开服务号Page"""
        ele_fwh = (By.CSS_SELECTOR, ".chat-title")
        WebDriverWait(self._driver, 10).until(ec.element_to_be_clickable(ele_fwh))
        ele_list = self._driver.find_elements(*ele_fwh)
        if len(ele_list) > 0:
            for i in range(len(ele_list)):
                if self._driver.find_elements(*ele_fwh)[i].text == "服务号":
                    self._driver.find_elements(*ele_fwh)[i].click()
                    break
        else:
            raise NoSuchElementException()
        return FWH(self._driver)


