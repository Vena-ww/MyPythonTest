from selenium.webdriver.common.by import By
from MyPythonTest.Python_test1.selenium_test.page.add_member_page import AddMember
from MyPythonTest.Python_test1.selenium_test.page.base_page import BasePage
from MyPythonTest.Python_test1.selenium_test.page.contact_page import Contact


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_contact(self):
        self.find(By.CSS_SELECTOR, '.frame_nav_item_title').click()
        return Contact(self._driver)

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, "node-type='addmember'").click()
        return AddMember(self._driver)