
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from MyPythonTest_Private.PythonTest_1.appium.page.basepage import BasePage
from MyPythonTest_Private.PythonTest_1.appium.page.usersetpage import UserSetPage


class SearchResult(BasePage):
    name = "沃尔"
    name_ele = (MobileBy.ID, "com.tencent.wework:id/g75")
    ele_list1 = (MobileBy.XPATH, f"//*[@text='{name}']")
    ele_member = (MobileBy.XPATH, f"//*[@text='{name}']")
    search_res = (MobileBy.XPATH, "//*[@text='无搜索结果']")

    def serach_result(self):
        self.find_and_sendkeys(self.name_ele, self.name)
        sleep(1)
        # 包括搜索框在内获取页面中有多少符合搜索条件的元素--要删除的名称，获取到一个列表
        elements = self.finds(self.ele_list1)
        # 计算得到的元素列表的长度
        beforenum = len(elements)
        if beforenum < 2:
            print("没有可删除的人员")
            return
        # 如果大于等于2，即表示有符合条件的元素存在，elements[1]表示元素列表的第二个元素，即除搜索框之外的第一个元素
        elements[1].click()  # 点击搜索结果进入个人信息页面
        return UserSetPage(self.driver)

    def last_result(self):
        # 从搜索框输入人员删除后会回到搜索结果页面，再次查找页面中有多少符合条件的元素
        self.find(self.ele_member)
        result_mes = self.find(self.search_res).text
        return result_mes


