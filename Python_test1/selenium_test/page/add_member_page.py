from selenium.webdriver.common.by import By
from MyPythonTest.Python_test1.selenium_test.page.base_page import BasePage
from MyPythonTest.Python_test1.selenium_test.page.contact_page import Contact


# 添加成员页面
class AddMember(BasePage):
    def add_member(self):
        self.find(By.ID, 'username').send_keys('用户1')
        self.find(By.ID, 'memberAdd_acctid').send_keys('11111')
        self.find(By.ID, 'memberAdd_phone').send_keys('13012345678')
        self.find(By.CSS_SELECTOR, '.qui_btn ww_btn js_btn_save').click()
        return Contact(self._driver)

    # def get_phone_error_message(self):
    #     return self.find(By.CSS_SELECTOR, 'ww_inputWithTips_tips').text