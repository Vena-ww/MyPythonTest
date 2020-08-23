from MyPythonTest.Python_test1.selenium_test.page.main_page import Main


class TestAddMember:
    def setup(self):
        self.main = Main()

    def test_contact_add_member(self):
        #           进入通讯录页面    进入添加成员        添加成员
        self.main.goto_contact().goto_add_member().add_member()

    def test_add_member(self):
        #             进入添加成员      添加成员
        self.main.goto_add_member().add_member()

    def teardown(self):
        self.main.base_quit()