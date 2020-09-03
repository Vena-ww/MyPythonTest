import os

import pytest
import yaml
from MyPythonTest_Private.PythonTest_1.appium.page.app import App


def get_contacts():
    path = os.path.dirname(__file__)
    data_path = os.path.dirname(path) + "/datas/contacts.yaml"
    with open(data_path, encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    return datas

class TestWechat:
    def setup(self):
        """
        启动APP
        """
        # 创建app.py中的App类的实例，调用App的start(),goto_main()方法启动应用进入首页
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        # 调用App的stop()方法，停止应用
        self.app.stop()

    # 添加联系人
    @pytest.mark.parametrize("name, gender, phone", get_contacts())
    def test_addcontact(self, name, gender, phone):
        #                    首页    进入通讯录页面     点击添加成员  点击手动输入添加进入编辑页面
        edit_messages = self.main.goto_addresslist().add_member().addmember_menu().edit_name(name).edit_gender(
            gender).edit_phone(phone).click_save()
        # 存入变量的页面调用获取toast的方法get_toast()
        toast_message = edit_messages.get_toast()
        assert toast_message == "添加成功"

    # 删除联系人
    def test_del_contact(self):
        #     首页     通讯录页面    点击搜索按钮后的页面
        last_text = self.main.goto_addresslist().search_menu().serach_result().user_set().del_user().last_result()
        assert last_text == "无搜索结果"
