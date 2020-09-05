from selenium.webdriver.common.by import By

from MyPythonTest.Python_test1.appium_test.PO_Framework.base_page import BasePage


class DemoPage(BasePage):
    _search_button = (By.ID, 'home_search')

    # todo:PO的数据驱动
    def login(self, username, password):
        pass

    def forget_password(self):
        pass

    def search(self, keyword):
        # self.find(self._search_button).click()
        self.po_run('search', keyword=keyword)   # keyword=keyword 代表传入的参数是字典形式
        return self

    def back_cancle(self):
        self.po_run('back')
        return self
