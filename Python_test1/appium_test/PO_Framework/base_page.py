import logging

import yaml
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _driver: WebDriver = None
    _current_element:WebElement = None

    def start(self):
        caps = {
            'platformName': 'android',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'deviceName': 'myPhone',
            'noReset': True
        }
        self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self._driver.implicitly_wait(10)
        return self

    def stop(self):
        self._driver.quit()

    def find(self, by):
        self._current_element = self._driver.find_element(*by)
        return self

    def click(self):
        self._current_element.click()
        return self

    def send_key(self, text):
        self._current_element.send_keys(text)
        return self

    def po_run(self, po_method):
        # 读取yaml文件
        with open('demo_page.yaml') as f:
            yaml_data = yaml.safe_load(f)
            # 遍历yaml文件查找一组字典 search
            for step in yaml_data[po_method]:
                # 遍历字典search中的列表数据--某一个操作：-id:name 等等
                if isinstance(step, dict):
                    # 如果列表中的数据是字典，遍历每组的key：id, click...
                    for key in step.keys():
                        if key == 'id':
                            locator = (By.ID, step[key])
                            self.find(locator)   # find()方法定义时的参数是元组，所以要传入元组类型的数据
                        elif key == 'click':
                            self.click()
                        elif key == 'send_keys':
                            self.send_key(step[key])
                        # todo:可以追加更多的关键词
                        else:
                            logging.error(f"错误：{step}")
