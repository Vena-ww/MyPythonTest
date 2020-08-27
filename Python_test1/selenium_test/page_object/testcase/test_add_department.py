from MyPythonTest.Python_test1.selenium_test.page_object.page.main_page import MainPage


class TestAddMember:
    def setup(self):
        self.main = MainPage()

    # 添加部门
    def test_add_department(self):
        # self.main.goto_contact().goto_add_department().add_department()
        result_list = self.main.goto_contact().goto_add_department().add_department().get_department()
        assert "第一部门" in result_list
    # 添加子部门

    # def teardown(self):
    #     self.main.close()
