# Time: 2020/11/10 15:57
# Author: jiangzhw
# FileName: test_login.py
from test_pcpro.page.main import Main


class TestLogin:
    def setup_class(self):
        self.main = Main()

    def test_login(self):
        login_page = self.main.enter_login_page()
        login_page.login_in_assert()

    def teardown_class(self):
        self.main.close_page()
