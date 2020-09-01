from appium.webdriver.common.mobileby import MobileBy

from MyPythonTest_Private.PythonTest_1.appium.page.basepage import BasePage


class MemberInvitePage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    addmember_menul_ele = (MobileBy.XPATH, "//*[@text='手动输入添加']")

    # 手动输入添加
    def addmember_menu(self):
        # 局部导入 防止循环导入
        from MyPythonTest_Private.PythonTest_1.appium.page.contactaddpage import ContactAddPage
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        # 封装到BasePage后的写法
        self.find_and_click(self.addmember_menul_ele)
        # 点击 手动输入添加 按钮 进入编辑页面
        return ContactAddPage(self.driver)

    # 添加联系人成功后获取到的toast信息
    def get_toast(self):
        # toast弹框
        # 打印当前页面的布局结构（xml结构）
        # print(self.driver.page_source)

        # toast_text = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        # return toast_text

        # 封装后：
        toast_text = self.get_toast_text()
        return toast_text
