
from time import sleep
from selenium.webdriver.common.by import By
from MyPythonTest.Python_test1.selenium_test.page_object.page.base import BasePage
from MyPythonTest.Python_test1.selenium_test.page_object.page.contact_page import ContactPage


class NewDepartmentPage(BasePage):
    # 添加部门
    def add_department(self):
        self.find(By.CSS_SELECTOR, ".ww_dialog_body [name='name']").send_keys("第一部门")
        # 点击选择所属部门
        self.find(By.CSS_SELECTOR, ".ww_dialog_body .js_toggle_party_list").click()
        # 选择部门中的根节点添加部门
        self.find(By.CSS_SELECTOR, ".js_party_list_container .jstree-open>.jstree-anchor").click()
        self.find(By.CSS_SELECTOR, "[d_ck='submit']").click()
        sleep(1)
        return ContactPage(self._driver)

    # 添加子部门
    def add_subdivision(self):
        self.find(By.CSS_SELECTOR, ".member_tag_dialog_inputDlg [name='name']").send_keys("子部门1")
        self.find(By.CSS_SELECTOR, ".ww_dialog_foot .ww_btn_Blue").click()
        sleep(1)
        return ContactPage(self._driver)
