from appium.webdriver.common.mobileby import MobileBy
from MyPythonTest_Private.PythonTest_1.appium.page.addresslistpage import AddressListPage
from MyPythonTest_Private.PythonTest_1.appium.page.basepage import BasePage


class MainPage(BasePage):
    # 初始化driver的方法封装到BasePage中，不需要再每个页面都初始化一遍
    # def __init__(self, driver):
    #     self.driver = driver

    # 将查找的元素及定位方式作为元组存放在变量中
    addresslist_eles = (MobileBy.XPATH, "//*[@text='通讯录']")

    # 从首页进入到通讯录页面
    def goto_addresslist(self):
        # 此种写法封装后是下面的形式
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()

        # 使用基类BasePage中封装的find_and_click()方法(find_element().click())
        self.find_and_click(self.addresslist_eles)
        # 进入通讯录页面
        return AddressListPage(self.driver)
