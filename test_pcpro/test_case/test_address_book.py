# Time: 2020/10/9 15:31
# Author: jiangzhw
# FileName: test_address_book.py
import pytest

from test_pcpro.page.main import Main


class TestAddressBook:
    """通讯录 case"""
    def setup(self):
        self.main = Main()

    def test_address_book(self):
        pass

    def teardown(self):
        self.main.close_page()
