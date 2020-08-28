
from time import sleep
from selenium.webdriver.common.by import By
from MyPythonTest_Private.PythonTest_1.page_object2.base import BasePage


class ContactPage(BasePage):
    def goto_add_member(self):
        from MyPythonTest.Python_test1.selenium_test.page_object.page.add_member_page import AddMember
        sleep(3)
        self.find(By.CSS_SELECTOR, '.ww_operationBar .js_add_member').click()
        # self.find(By.XPATH, "//*[@class='ww_operationBar']/a[@class='qui_btn ww_btn js_add_member']").click()
        # sleep(3)
        return AddMember(self._driver)

    def get_member_list(self):
        name_list = self._driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        list1 = []
        for name in name_list:
            list1.append(name.text)
        return list1

    def goto_add_department(self):
        from MyPythonTest_Private.PythonTest_1.page_object2.new_department_page import NewDepartmentPage
        sleep(1)
        self.find(By.CSS_SELECTOR, '.js_create_dropdown').click()
        sleep(0.5)
        self.find(By.CSS_SELECTOR, '.js_create_dropdown_container .js_create_party').click()
        return NewDepartmentPage(self._driver)

    def get_department(self):
        result = self._driver.find_elements(By.CSS_SELECTOR, "[class='jstree-children']>.jstree-node :nth-child(3)")
        list_depart = []
        for name in result:
            list_depart.append(name.text)
        print(list_depart)
        return list_depart

    def goto_add_subdivision(self):
        from MyPythonTest_Private.PythonTest_1.page_object2.new_department_page import NewDepartmentPage
        sleep(1)
        self.find(By.CSS_SELECTOR, ".js_party_edit .js_add_sub_party").click()
        return NewDepartmentPage(self._driver)

    def get_subdivision(self):
        # 获取最后的一个部门名称，即是最新添加的
        sub_name = self.find(By.CSS_SELECTOR, "[class='jstree-children']>.jstree-node:last-child").text
        # print(sub_name)
        return sub_name
