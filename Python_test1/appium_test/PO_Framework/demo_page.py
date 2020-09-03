from selenium.webdriver.common.by import By

from MyPythonTest.Python_test1.appium_test.PO_Framework.base_page import BasePage


class DemoPage(BasePage):
    _search_button = (By.ID, 'home_search')

    # todo:PO的数据驱动
    def login(self, username, password):
        pass

    def forget_password(self):
        pass

    def search(self):
        # self.find(self._search_button).click()
        self.po_run('search')
        return self

