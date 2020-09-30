# Time: 2020/9/27 16:04
# Author: jiangzhw
# FileName: base_page.py
import sys
import logging
import win32gui
import win32con
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
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
            options = webdriver.ChromeOptions()
            # options.add_argument("--remote-debugging-port=9222")  # open devtools for operator element
            # options.add_experimental_option('w3c', False)
            path = "D:/driver/chromedriver_win32_80.0.3987.16/chromedriver.exe"
            # options.set_capability('platform', 'WINDOWS')  # test windows app
            # options.set_capability('version', '10')  # window version
            options.set_capability("os", "Windows")
            options.set_capability('os_version', '10')
            options.binary_location = u"C:/Users/jiangzhw01/AppData/Local/Programs/ccwork-pc/云上协同 Alpha.exe"  # start up app path
            self._driver = webdriver.Chrome(executable_path=path, options=options)
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

    def mouse_hover(self, ele):
        """鼠标悬停"""
        ActionChains(self._driver).move_to_element(ele).perform()

    def close_page(self):
        """关闭页面"""
        sleep(8)
        self._driver.quit()

    def login_in(self, username=None, pwd=None, group=None):
        """login in """
        if group is not None:
            self._driver.find_element(By.CSS_SELECTOR, ".login-head .cc-btn").click()
            self._driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入组织号"]').send_keys(group)
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

    def login_out(self):
        """login out"""
        ele_avatar = (By.CSS_SELECTOR, ".user-avatar img")
        self.mouse_hover(ele_avatar)
        self._driver.find_element(By.LINK_TEXT, "登出").click()

    def switch_to_window(self, index):
        """切换window窗口"""

        if len(self._driver.window_handles) > 1:
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
            self._driver.find_element(*ele).is_displayed()
        except NoSuchElementException as e:
            self._logger.error("{} element is not found !".format(ele))
            return False
        else:
            self._logger.info("元素存在!")
            return True

    def set_window_size(self, width, height):
        """设置窗口大小"""
        handler = self.get_handlers()
        print(handler)
        win32gui.SetWindowPos(handler, None, 0, 0, width, height, win32con.SWP_NOSENDCHANGING | win32con.SWP_SHOWWINDOW)

    def get_handlers(self):
        hdl = win32gui.GetForegroundWindow()
        return hdl
