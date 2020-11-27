# Time: 2020/9/27 16:04
# Author: jiangzhw
# FileName: base_page.py
import sys
import logging

import win32api
import win32gui
import win32con
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Base Page"""
    _logger = logging.getLogger('log')
    _logger.setLevel(logging.DEBUG)
    print(_logger)

    # 调用模块时,如果错误引用，比如多次调用，每次会添加Handler，造成重复日志，这边每次都移除掉所有的handler，后面在重新添加，可以解决这类问题
    if _logger.hasHandlers():
        print(_logger.hasHandlers())
        for i in _logger.handlers:
            _logger.removeHandler(i)

    # file log 写入文件配置
    formatter = logging.Formatter(
        '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # 日志的格式
    fh = logging.FileHandler(r'test_logger.log', encoding='utf-8')  # 日志文件路径文件名称，编码格式
    fh.setLevel(logging.DEBUG)  # 日志打印级别
    fh.setFormatter(formatter)
    _logger.addHandler(fh)

    # console log 控制台输出控制
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    _logger.addHandler(ch)

    def __init__(self, driver: WebDriver = None):
        """init fun"""
        # 初始化driver
        if driver is None:
            path = "D:/driver/chromedriver/chromedriver_win32_85.0.4183.102.exe"
            options = webdriver.ChromeOptions()
            capabilities = DesiredCapabilities.CHROME.copy()
            capabilities['platform'] = "WINDOWS"
            capabilities['version'] = "10"
            # options.set_capability('platform', 'WINDOWS')  # test windows app
            # options.set_capability('version', '10')  # window version
            # capabilities['chromedriverExecutable'] = path 不可行
            # todo: selenium 实现和appium chromedriverExecutable类似自动选择webdriver功能
            capabilities['executable_path'] = path
            # options.add_argument("--remote-debugging-port=9222")  # open devtools for operator element
            # options.add_experimental_option('w3c', False)
            options.binary_location = u"C:/Users/jiangzhw01/AppData/Local/Programs/ccwork-pc/云上协同 Dev.exe"  # start up app path
            self._driver = webdriver.Chrome(executable_path=path, desired_capabilities=capabilities, options=options)
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

    def mouse_hover(self, ele):
        """鼠标悬停"""
        ActionChains(self._driver).move_to_element(self.find(ele)).perform()

    def close_page(self):
        """关闭页面"""
        sleep(10)
        self._driver.quit()

    def login_in(self, username=None, pwd=None, group=None):
        """login in """
        if group is not None:
            self._driver.find_element(By.CSS_SELECTOR, ".login-head .cc-btn").click()
            self._driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入组织代号"]').send_keys(group)
            self._driver.find_element(By.CSS_SELECTOR, ".btn-bind").click()
            ele_login = (By.CSS_SELECTOR, ".login-btn")
            WebDriverWait(self._driver, 10).until(ec.element_to_be_clickable(ele_login))
        if username is not None:
            self._driver.find_element(By.CSS_SELECTOR, '.cc-input__inner[placeholder="请输入账号"]').clear()
            self._driver.find_element(By.CSS_SELECTOR, '.cc-input__inner[placeholder="请输入账号"]').send_keys(username)
        if pwd is not None:
            self._driver.find_element(By.CSS_SELECTOR, '.cc-input__inner[placeholder="请输入密码"]').clear()
            self._driver.find_element(By.CSS_SELECTOR, '.cc-input__inner[placeholder="请输入密码"]').send_keys(pwd)

        self._driver.find_element(By.CSS_SELECTOR, "button.login-btn").click()
        self.switch_to_window(1)

    def switch_to_window(self, index):
        """切换window窗口"""

        if len(self._driver.window_handles) > index:
            print(self._driver.window_handles)
            self._driver.switch_to.window(self.get_window_handles(index))
        else:
            sleep(5)
            print(self._driver.window_handles)
            self._driver.switch_to.window(self.get_window_handles(index))

    def get_window_handles(self, index):
        """selenium获取window窗口信息"""
        if index <= len(self._driver.window_handles):
            return self._driver.window_handles[index]
        else:
            raise Exception("Error:index is outside.")

    def is_element_exit(self, ele):
        """判断元素是否存在"""
        try:
            self.find(ele).is_displayed()
        except NoSuchElementException as e:
            # self._logger.error("{} element is not found !".format(ele))
            return False
        else:
            self._logger.info("元素存在!")
            return True

    def wait(self, timeout, method):
        """"wait method """
        # WebDriverWait默认等待时间 poll_frequency = 0.5
        WebDriverWait(self._driver, timeout).until(method)

    def set_window_size(self, width, height):
        """设置窗口大小"""
        handle = self.get_handles()
        print(handle)
        win32gui.SetWindowPos(handle, None, 0, 0, width, height, win32con.SWP_NOSENDCHANGING | win32con.SWP_SHOWWINDOW)

    def get_handles(self):
        """win32gui 获取窗口句柄"""
        return win32gui.GetForegroundWindow()

    def get_mouse_pos(self):
        """win32api 获取鼠标位置"""
        return win32api.GetCursorPos()

    def find(self, locator):
        """find_element method 改造"""
        if isinstance(locator, tuple):
            return self._driver.find_element(*locator)
        else:
            self._driver.find_element(locator)

    # Todo:封装find_elements()方法
    def finds(self, locator):
        """find_elements method 改造"""
        pass

    def is_ele_clickable(self, locator):
        """判断元素是否可点击
        :param locator：ele locator
        :return: bool 当元素可点击返回True，元素不可点击返回False
        """
        isClick = False
        if self.find(locator).is_displayed():
            try:
                self.find(locator).click()
            except:
                self._logger.error("元素不可点击!")
            else:
                self._logger.info("元素可点击!")
                isClick = True
        return isClick

    def wait_element_display(self, element, time_out=3, message=''):
        """
        等待element元素消失，成功消失返回True，否则返回False
        :param message: TimeoutException message
        :param driver:  selenium.webdriver.remote.webdriver.WebDriver
        :param element: selenium.webdriver.remote.webelement.WebElement
        :param time_out: 隐式等待时间
        :return: bool 当元素成功消失返回True，元素未消失返回False
        """
        inti = 0
        while inti < 3:
            # 当元素消失的时候返回True，进行下一步操作
            try:
                # Todo : 获取隐式等待时间为timeout
                self.wait(time_out, ec.invisibility_of_element(element))
                boolean = True
            except TimeoutException:
                boolean = False
            if boolean:
                self._logger.info("该元素已经消失!")
                break
            else:
                self._logger.warning("该元素还未消失!")
                inti += 1
        if inti >= 3:
            self._logger.error("3次判断后该元素还未消失!" + element.__str__())
            # print(type(element.__str__()))
            raise TimeoutException(message)
        else:
            return True

    def search(self, name):
        """首页搜索功能"""
        search = (By.CSS_SELECTOR, '.chat-list-search input[placeholder="搜索"]')
        self.wait(10, ec.presence_of_element_located(search))
        self.find(search).send_keys(name)
