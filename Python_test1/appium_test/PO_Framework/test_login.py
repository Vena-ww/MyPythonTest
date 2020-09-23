import logging

import pytest

from MyPythonTest.Python_test1.appium_test.PO_Framework.demo_page import DemoPage
from MyPythonTest.Python_test1.appium_test.PO_Framework.utils import Utils


class TestLogin:
    data = Utils.load_file('test_search.yaml')

    def setup_class(self):
        self.demo = DemoPage()
        self.demo.start()

    def setup(self):
        pass

    def teardown(self):
        self.demo.back_cancle()

    def teardown_class(self):
        self.demo.stop()

    # todo:测试数据的数据驱动（存放在yaml文件）
    @pytest.mark.parametrize('username, password', [
        ("user1", "pass1"),
        ('user2', 'pass2')
    ])
    def test_login(self, username, password):
        # todo:测试步骤的数据驱动（可以存放在yaml文件中）
        self.demo.login(username, password)
        assert 1 == 1

    # @pytest.mark.parametrize('keyword', [
    #     'alibaba',
    #     # 'baidu',
    #     # 'jd'
    # ])
    @pytest.mark.parametrize(data['keys'], data['values'])
    def test_search(self, keyword):
        # logging.info(keyword)
        self.demo.search(keyword)
