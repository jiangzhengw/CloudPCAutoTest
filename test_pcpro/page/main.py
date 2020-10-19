# Time: 2020/9/27 11:36
# Author: jiangzhw
# FileName: main.py
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec

from test_pcpro.page.base_page import BasePage
from test_pcpro.page.fwh import FWH


class Main(BasePage):
    """Main page"""

    def fwh_click(self, timeout):
        """点击打开服务号Page"""
        ele_fwh = (By.CSS_SELECTOR, ".chat-title")
        self.wait(10, ec.element_to_be_clickable(ele_fwh))
        sleep(3)
        ele_list = self._driver.find_elements(*ele_fwh)
        if len(ele_list) > 0:
            for i in range(len(ele_list)):
                if self._driver.find_elements(*ele_fwh)[i].text == "服务号":
                    print(self._driver.find_elements(*ele_fwh)[i].text)
                    self._driver.find_elements(*ele_fwh)[i].click()
        else:
            raise NoSuchElementException()
        return FWH(self._driver)

    def test_method(self):
        self._driver.find_elements(By.CSS_SELECTOR, 'span[class="chat-title"]')[2].click()
        self._driver.find_element(By.CSS_SELECTOR, '.chat-input-wrapper').send_keys("webdriver")
        self._driver.find_element(By.CSS_SELECTOR, '.chat-input-wrapper').send_keys(Keys.ENTER)
