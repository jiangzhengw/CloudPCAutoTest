# Time: 2020/9/27 11:30
# Author: jiangzhw
# FileName: test_chat.py
import os
import shutil

import pytest

from test_pcpro.page.main import Main

search_data = [
    '苏爽',
    '哈哈哈哈哈'
]


class TestChat:
    def setup_class(self):
        self.main = Main()
        self.main.login_in(username="jiangzhw01", pwd="552165844zjx**", group="inspur")

    def test_login_out(self):
        self.main.login_out()

    def test_chat_fwh(self):
        fwh_page = self.main.fwh_click()
        fwh_page.assert_fwh()
        fwh_page.click_one_fwh("测试服务号")
        fwh_page.assert_fwh_detail("测试服务号")
        fwh_page.fwh_operation()

    def test_notice(self):
        notice_page = self.main.notice_click()
        notice_page.assert_notice()

    def test_personal_info(self):
        self.main.person_info_operation()

    @pytest.mark.parametrize('name', search_data)
    def test_search(self, name):
        self.main.precise_search(name)

    def test_new_chat(self):
        pass

    def teardown_class(self):
        self.main.close_page()


if __name__ == '__main__':
    pytest.main("test_chat.py")
    # 生成html报告文件
    # os.system("allure generate -c D:/PythonPro/CloudPCAutoTest/test_pcpro/reports")
    # 为避免文件占用使用强制删除，再新建目录的方式
    # shutil.rmtree("D:/PythonPro/CloudPCAutoTest/test_pcpro/reports")
    # os.mkdir('D:/PythonPro/CloudPCAutoTest/test_pcpro/reports')
