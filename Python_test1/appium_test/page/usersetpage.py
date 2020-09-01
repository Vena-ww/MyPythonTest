from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from MyPythonTest_Private.PythonTest_1.appium.page.basepage import BasePage
from MyPythonTest_Private.PythonTest_1.appium.page.deluserpage import DelUserPage


class UserSetPage(BasePage):
    set_page = (MobileBy.ID, "com.tencent.wework:id/hjz")
    edit_member = (MobileBy.XPATH, "//*[@text='编辑成员']")

    def user_set(self):
        # 点击右上角的三个点点，进入个人信息设置页面
        self.find_and_click(self.set_page)
        # 点击编辑成员按钮
        self.find_and_click(self.edit_member)
        sleep(1)
        return DelUserPage(self.driver)
