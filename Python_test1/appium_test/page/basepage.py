'''
基类：存放最基本、通用的方法。
实例化driver，find。。。。
'''
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    # 获取日志信息
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        '''
        初始化driver
        '''
        self.driver = driver

    # 查找元素
    def find(self, locator):
        logging.info(locator)
        return self.driver.find_element(*locator)

    def finds(self, locator):
        logging.info(locator)
        return self.driver.find_elements(*locator)

    # 查找元素并点击
    def find_and_click(self, locator):
        logging.info("点击按钮")
        self.find(locator).click()

    # 查找元素并输入
    def find_and_sendkeys(self, locator, value):
        logging.info("输入内容")
        self.find(locator).send_keys(value)

    # 滚动查找
    def find_by_scroll_and_click(self, text):
        logging.info("滚动查找并点击")
        logging.info(text)
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector()'
                   '.scrollable(true).instance(0))'
                   '.scrollIntoView(new UiSelector()'
                   f'.text("{text}").instance(0));')
        self.find(element).click()

        # 添加联系人成功后获取到的toast信息

    def get_toast_text(self):
        logging.info("获取toast")
        text = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        logging.info(text)
        return text
