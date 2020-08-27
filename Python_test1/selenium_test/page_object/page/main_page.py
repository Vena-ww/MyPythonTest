from selenium.webdriver.common.by import By
from MyPythonTest.Python_test1.selenium_test.page_object.page.add_member_page import AddMember
from MyPythonTest.Python_test1.selenium_test.page_object.page.base import BasePage
from MyPythonTest.Python_test1.selenium_test.page_object.page.contact_page import ContactPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_contact(self):
        self.find(By.ID, "menu_contacts").click()
        return ContactPage(self._driver)

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, "[node-type='addmember']").click()
        return AddMember(self._driver)

