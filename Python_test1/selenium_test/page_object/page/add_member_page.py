
from selenium.webdriver.common.by import By
from MyPythonTest.Python_test1.selenium_test.page_object.page.base import BasePage
from MyPythonTest.Python_test1.selenium_test.page_object.page.contact_page import ContactPage


class AddMember(BasePage):
    def add_member(self, username, phone, acctid):
        self.find(By.ID, 'username').send_keys(username)
        self.find(By.ID, 'memberAdd_acctid').send_keys(acctid)
        self.find(By.ID, 'memberAdd_phone').send_keys(phone)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        return ContactPage(self._driver)

    def get_phone_error_message(self):
        return self._driver.find_element(By.CSS_SELECTOR, '.ww_inputWithTips_WithErr .ww_inputWithTips_tips').text
