# Time: 2020/9/27 11:30
# Author: jiangzhw
# FileName: test_chat.py
import pytest
from test_pcpro.page.main import Main


class TestChat:
    def setup(self):
        self.main = Main()

    def test_chat_fwh(self):
        self.main.login_in(username="jiangzhw01", pwd="..552165844zjx", group="inspur")
        self.main.switch_to_window(1)
        fwh_page = self.main.fwh_click(10)
        fwh_page.assert_fwh()
        fwh_page.click_one_fwh("测试服务号")
        fwh_page.assert_fwh_detail("测试服务号")
        fwh_page.fwh_operation()

    def teardown(self):
        self.main.close_page()


if __name__ == '__main__':
    pytest.main("test_chat.py")
