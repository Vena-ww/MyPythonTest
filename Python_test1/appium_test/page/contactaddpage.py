# 局部导入在方法中，全局导入在类外
# 编辑联系人信息页面
from appium.webdriver.common.mobileby import MobileBy

from MyPythonTest_Private.PythonTest_1.appium.page.basepage import BasePage


class ContactAddPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    name_ele = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText")
    gender_ele = (MobileBy.XPATH, "//*[@text='男']")
    male_ele = (MobileBy.XPATH, "//*[@text='男']")
    female_ele = (MobileBy.XPATH, "//*[@text='女']")
    phone_ele = (MobileBy.ID, "com.tencent.wework:id/f9s")
    save_ele = (MobileBy.ID, "com.tencent.wework:id/hk6")

    def edit_name(self, name):
        # self.driver.find_element(MobileBy.XPATH,
        #                          "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)

        # 封装到BasePage中后的写法：
        self.find_and_sendkeys(self.name_ele, name)
        return self  # 编辑姓名后还停留在当前页 所以return self 继续进行下一步操作

    def edit_gender(self, gender):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        # if gender == "男":
        #     self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        # else:
        #     self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        # 封装到BasePage中后的写法
        self.find_and_click(self.gender_ele)
        if gender == "男":
            self.find_and_click(self.male_ele)
        else:
            self.find_and_click(self.female_ele)
        return self  # 编辑性别后停留在当前页

    def edit_phone(self, phone):
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f9s").send_keys(phone)

        self.find_and_sendkeys(self.phone_ele, phone)   # 封装后
        return self  # 编辑号码后停留在当前页

    # 点击保存后返回到上一个页面，(有手动输入添加按钮的页面)
    def click_save(self):
        # 局部导入
        from MyPythonTest_Private.PythonTest_1.appium.page.memberinvitepage import MemberInvitePage
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hk6").click()  # 保存按钮
        self.find_and_click(self.save_ele)    # 封装后
        return MemberInvitePage(self.driver)  # 返回到上一页
