from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


# 像添加和删除内容一类比较重要的会改变原有内容的用例需要断言
# 其他的像是页面跳转、获取文本信息一类的就不需要断言了
class TestWechat:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_send_messages(self):
        pass

    def test_add_contact(self):
        """
        企业微信：添加联系人测试用例
        前提条件
            已登录状态（ noReset=True）
        打开用例：
            1、打开【企业微信】应用
            2、进入【通讯录】
            3、点击【添加成员】
            4、在添加成员页面点击【手动输入添加】
            5、输入【姓名】【性别】【手机号】
            6、点击【保存】
            7、验证保存成功
        """
        name = "雷神"
        gender = "男"
        phone = "13011115678"

        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        if gender == "男":
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f9s").send_keys(phone)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hk6").click()  # 保存按钮
        sleep(2)

        # toast弹框
        # 打印当前页面的布局结构（xml结构）
        # print(self.driver.page_source)
        toast_text = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert "添加成功" == toast_text

    # 删除通讯录中的联系人
    def test_delete_contact(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='雷神']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hjz").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        sleep(2)
        # 点击通讯录页面的搜索按钮
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hk9").click()
        # 在搜索框输入要查找的联系人
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/g75").send_keys("雷神")
        # 如果输入联系人后页面显示 无搜索结果，即为删除成功
        result_mes = self.driver.find_element(MobileBy.XPATH, "//*[@text='无搜索结果']").text
        assert "无搜索结果" == result_mes
