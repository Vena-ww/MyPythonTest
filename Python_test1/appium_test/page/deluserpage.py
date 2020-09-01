from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from MyPythonTest_Private.PythonTest_1.appium.page.basepage import BasePage


class DelUserPage(BasePage):
    delmember_text = "删除成员"
    makesure = (MobileBy.XPATH, "//*[@text='确定']")

    def del_user(self):
        from MyPythonTest_Private.PythonTest_1.appium.page.searchpage import SearchResult
        # 根据页面分辨率可能需要滚动查找元素
        self.find_by_scroll_and_click(self.delmember_text)  # 点击删除按钮
        self.find_and_click(self.makesure)    # 点击确认
        sleep(1)
        return SearchResult(self.driver)
