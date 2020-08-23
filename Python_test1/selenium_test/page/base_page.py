from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


# BasePage类是所有page object的父类，为子类提供公共的方法。
# 此处的BasePage提供初始化driver和退出driver，类中使用__init__初始方法进行初始化操作。
# 包括driver的复用，driver的赋值，全局等待(隐式等待)的设置等。
class BasePage:
    _base_url = ""

    # driver: WebDriver--代表driver类型，方便类型识别
    def __init__(self, driver: WebDriver = None):
        # 此处对driver进行复用，如果不存在driver，就构造一个新的
        if driver is None:
            # 首次使用时构造新driver，index页面需要用。
            # 打开端口，复用浏览器，(仅支持Chrome浏览器)
            option = Options()
            option.debugger_address = 'localhost:9222'
            self._driver = webdriver.Chrome(options=option)
        else:
            # login与register等页面需要用这个方法，避免重复构造driver
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)
        self._driver.implicitly_wait(4)  # 设置隐式等待

    # 在用例方法中调用,关闭浏览器
    def base_quit(self):
        self._driver.quit()

    # 定义find_element()方法，在其他模块定位元素时可以直接调用find()方法
    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)