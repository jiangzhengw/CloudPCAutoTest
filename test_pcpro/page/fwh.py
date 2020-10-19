# Time: 2020/9/27 14:45
# Author: jiangzhw
# FileName: fwh.py
from time import sleep
import win32api
import win32con
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec

from test_pcpro.page.base_page import BasePage
from test_pcpro.page.email import EMAIL


class FWH(BasePage):
    """服务号 Page"""

    def assert_fwh(self):
        """服务号页面断言"""
        fwh_list = []
        sleep(3)
        l = len(self._driver.find_elements(By.CSS_SELECTOR, ".chat-service-title"))
        if l > 0:
            for i in range(l):
                fwh_list.append(self._driver.find_elements(By.CSS_SELECTOR, ".chat-service-title")[i].text)
        else:
            raise Exception("{} is not found!".format("服务号"))
        assert "测试服务号" in fwh_list
        assert "服务号" == self._driver.find_element(By.CSS_SELECTOR, '.chat-detail-title span').text
        return self._driver.find_elements(By.CSS_SELECTOR, ".chat-service-title")

    def click_fwh(self, index=0):
        """打开第一个服务号"""
        print(self.assert_fwh())
        if len(self.assert_fwh()) > 0:
            self.assert_fwh()[index].click()
        else:
            raise Exception("{} is not found!".format("服务号"))

    def click_one_fwh(self, fwh_name):
        """打开某服务号"""
        # todo: 点击实现方法待优化
        fwh = self.assert_fwh()
        sleep(3)
        ll = len(fwh)
        if ll > 0:
            for i in range(ll):
                if self._driver.find_elements(By.CSS_SELECTOR, ".chat-service-title")[i].text == fwh_name:
                    self.assert_fwh()[i].click()
        else:
            raise Exception("{} is not found!".format("服务号"))

    def assert_fwh_detail(self, fwh_name):
        """服务号详情断言"""
        assert fwh_name == self._driver.find_element(By.CSS_SELECTOR, '.chat-detail-title-back span').text
        ele_emo = (By.CSS_SELECTOR, '.icon-chat-face')
        ele_prc_scr = (By.CSS_SELECTOR, 'button[title="截屏（Ctrl+Alt+X）"]')
        ele_micro_mail = (By.CSS_SELECTOR, 'button[title="微邮"]')
        ele_upload = (By.CSS_SELECTOR, 'button[title="上传文件"]')
        ele_attach = (By.CSS_SELECTOR, 'button[title="附件列表"]')
        # ele_submit = (By.CSS_SELECTOR, '[aria-describedby="cc-popover-2854"]')
        self.is_element_exit(ele_emo)
        self.is_element_exit(ele_prc_scr)
        self.is_element_exit(ele_micro_mail)
        self.is_element_exit(ele_upload)
        self.is_element_exit(ele_attach)
        # self.is_element_exit(ele_submit)

    def fwh_emo_operate(self, ele_emo, number):
        """服务号聊天-表情"""
        # WebDriverWait(self._driver, 10).until(ec.element_to_be_clickable(ele_emoji_item))
        for i in range(number):
            self._driver.find_element(*ele_emo).click()
            self._driver.find_element(By.CSS_SELECTOR, f'.chat-emoji-container div:nth-child({i + 1})').click()
            sleep(0.5)
        # ele_submit = (By.CSS_SELECTOR, '[aria-describedby="cc-popover-2854"]')
        # self._driver.find_element(*ele_submit).click()
        # self._driver.find_element(By.CSS_SELECTOR, '.chat-input-wrapper').send_keys("webdriver" + Keys.ENTER)

    def pri_scr(self):
        """服务号聊天-截屏"""
        # PC端点击坐标和左右键点击都无效，大概率不支持，暂不做详细操作
        action = ActionChains(self._driver)
        self._driver.find_element(By.CSS_SELECTOR, 'span[title="设置"]').click()
        self._driver.find_element(By.CSS_SELECTOR, 'span[class="cc-checkbox-label"]').click()
        self._driver.find_element(By.CSS_SELECTOR, '.icon-chat-capture').click()
        # action.move_by_offset(200, 100).click().perform()  # 鼠标左键点击， 200为x坐标， 100为y坐标
        # action.move_by_offset(500, 500).context_click().perform()    # 右键点击
        sleep(3)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

    def upload_files(self):
        """服务号聊天-上传文件"""
        self._driver.find_element(By.CSS_SELECTOR, '.icon-chat-appendix').click()
        # self._driver.save_screenshot("")
        sleep(3)
        win32api.keybd_event(27, 0, 0, 0)

    def we_email(self):
        """"服务号聊天-微邮"""
        email = (By.CSS_SELECTOR, 'button[title="微邮"]')
        self.wait(10, ec.element_to_be_clickable(email))
        self._driver.find_element(*email).click()
        return EMAIL(self._driver)

    def fwh_operation(self):
        """服务号内操作"""
        """
        ele_emo = (By.CSS_SELECTOR, '.icon-chat-face')
        self.fwh_emo_operate(ele_emo, 6)
        self._driver.find_element(By.CSS_SELECTOR, '.chat-input-wrapper').send_keys(Keys.ENTER)
        self.pri_scr()
        self.upload_files()
        """
        email_page = self.we_email()
        self.switch_to_window(2)
        email_page.email_assert()
