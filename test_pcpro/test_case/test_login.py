# Time: 2020/11/10 15:57
# Author: jiangzhw
# FileName: test_login.py
import pytest

from test_pcpro.page.main import Main

login_data = [
    ("", "", "账号和密码不能为空！"),
    ("test1", "12345", "请输入6-40位的密码"),
    ("test2", "123456", "用户不存在"),
    ("17864199426", "哈哈哈哈", "请输入6-40位的密码"),
    ("17864199426", "*&*&^%%", "用户名或密码错误"),
    ("17864199426", "哈哈哈哈哈哈", "用户名或密码错误"),
    ("17864199426", "12345678901234567890123456789012345678901234567890", "请输入6-40位的密码")
]

remember_data = [
    ("17864199426", "123456a?", False),
    ("17864199426", "123456a?", True)
]

group_code = [
    "", "inspur", "INSPUR", "Inspur", "\000inspur", "inspur\000", "ins\000pur", "测试"
]


class TestLogin:
    def setup_class(self):
        self.main = Main()
        self.login_page = self.main.enter_login_page()
        self.login_page.clear_bind_group()

    def test_login_page(self):
        self.login_page.login_in_assert()

    @pytest.mark.parametrize('name,pwd,toast', login_data)
    def test_login_input(self, name, pwd, toast):
        self.login_page.input_login_msg(name, pwd)
        self.login_page.login_submit()
        self.login_page.login_toast_assert(toast)

    @pytest.mark.parametrize('name,pwd,rescue', remember_data)
    def test_remember_pwd(self, name, pwd, rescue):
        self.login_page.remember_pwd(rescue=False)
        self.login_page.input_login_msg(name, pwd)
        self.login_page.remember_pwd(rescue)
        self.login_page.login_submit()
        self.main.switch_to_window(1)
        self.main.login_out()
        self.main.switch_to_window(0)
        pytest.assume(self.login_page.pwd_not_empty() is rescue)

    @pytest.mark.parametrize('group_code', group_code)
    def test_change_group(self):
        self.login_page.change_group(group_code)

    def teardown_class(self):
        self.main.close_page()
