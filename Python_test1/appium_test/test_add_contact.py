from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


def get_contacts():
    with open("./datas/contacts.yaml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    return datas


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

    @pytest.mark.parametrize('name, gender, phone', get_contacts())
    def test_add_contact(self, name, gender, phone):
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
        # name = "雷神"
        # gender = "男"
        # phone = "13011115678"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 直接定位 一旦联系人过多，添加成员按钮就会被挤到下一屏的位置，无法定位到，所以采取下面的方式比较完善
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        # 根据页面分辨率可能需要滚动查找元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
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
        """
        此处是没有滚动查找元素，不够完善
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
        """
        # 滚动查找元素
        name = "雷神"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hk9").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/g75").send_keys(name)
        sleep(1)
        # 包括搜索框在内获取页面中有多少符合搜索条件的元素--要删除的名称，获取到一个列表
        elements = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        # 计算得到的元素列表的长度
        beforenum = len(elements)
        # print(beforenum)
        # 如果长度小于2，即表示除搜索框外，没有其他符合条件的元素，提示没有可删除的人员
        if beforenum < 2:
            print("没有可删除的人员")
            return
        # 如果大于等于2，即表示有符合条件的元素存在，
        # elements[1]表示获取到元素列表的第二个元素，即除搜索框之外的第一个元素
        elements[1].click()
        # 点击右上角的三个点点，进入个人信息设置页面
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hjz").click()
        # 点击编辑成员按钮
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        sleep(1)
        # 根据页面分辨率可能需要滚动查找元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("删除成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        sleep(1)
        # 从搜索框输入人员删除后会回到搜索结果页面，所以直接查找页面中有多少符合条件的元素即可
        elements1 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        # 获取到当前页面元素的列表长度
        afternum = len(elements1)
        # 如果当前页面元素的长度与删除前的元素长度-1之后的结果是相等的，则表示删除成功
        assert afternum == beforenum - 1
