from appium.webdriver.common.mobileby import MobileBy
from MyPythonTest_Private.PythonTest_1.appium.page.basepage import BasePage
from MyPythonTest_Private.PythonTest_1.appium.page.memberinvitepage import MemberInvitePage


class AddressListPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    addmember_text = "添加成员"

    # 点击 添加成员
    def add_member(self):
        '''
        添加成员
        '''
        # 直接定位一旦联系人过多，添加成员按钮就会被挤到下一屏的位置，无法定位到
        # 根据页面分辨率可能需要滚动查找元素
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()

        # 封装到BasePage后的写法
        self.find_by_scroll_and_click(self.addmember_text)
        # 进入到 点击添加成员后跳转的页面 有手动输入添加按钮
        return MemberInvitePage(self.driver)

    menu_ele = (MobileBy.ID, "com.tencent.wework:id/hk9")

    # 点击搜索按钮
    def search_menu(self):
        from MyPythonTest_Private.PythonTest_1.appium.page.searchpage import SearchResult
        self.find_and_click(self.menu_ele)
        return SearchResult(self.driver)

