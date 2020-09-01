"""
App类：
app常用的方法：启动应用，重启应用，关闭应用
"""
from appium import webdriver

from MyPythonTest_Private.PythonTest_1.appium.page.basepage import BasePage
from MyPythonTest_Private.PythonTest_1.appium.page.mainpage import MainPage


class App(BasePage):
    def start(self):
        '''
        启动应用，如果driver已经被实例化，就复用已有的driver
        如果driver=None，就实例化创建driver
        '''
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # 隐式等待
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()   # 启动caps里设置的appPackage，appActivity
            # self.driver.start_activity()  # 可跨应用启动，启动任何一个appPackage和appActivity
        # 返回自身，调用自己类的goto_main()方法进入首页
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    # 进入首页
    def goto_main(self) -> MainPage:
        return MainPage(self.driver)
