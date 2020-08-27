from MyPythonTest_Private.PythonTest_1.page_object2.add_member_page import AddMember
from MyPythonTest_Private.PythonTest_1.page_object2.main_page import MainPage


class TestAddMember:
    def setup(self):
        self.main = MainPage()

    def test_add_member(self):
        #             首页    跳转到添加成员     添加成员          传入的参数             获取添加成员后的姓名列表
        result = self.main.goto_add_member().add_member('user1', '13011112222', 'id11').get_member_list()
        assert 'user1' in result

    def test_add_member_fail(self):
        self.main.goto_add_member().add_member('user2', '1111', 'id12')
        result = AddMember(self.main._driver).get_phone_error_message()
        # print(result)
        assert "请填写正确的手机号码" == result

    def test_contact_add(self):
        #    首页  跳转到通讯录页面    跳转到添加成员      添加成员
        self.main.goto_contact().goto_add_member().add_member('user3', '13011113333', 'id13')

    # def teardown(self):
    #     self.main.close()
