from selenium.webdriver.common.by import By

from MyPythonTest.Python_test1.selenium_test.page.base_page import BasePage


# 通讯录页面
class Contact(BasePage):
    def goto_add_member(self):
        from MyPythonTest.Python_test1.selenium_test.page.add_member_page import AddMember
        # self.find(By.CSS_SELECTOR, '.qui_btn ww_btn js_add_member').click()
        return AddMember(self._driver)