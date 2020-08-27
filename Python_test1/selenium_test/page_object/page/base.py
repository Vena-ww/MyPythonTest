from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            option = Options()
            # 命令行输入：chrome --remote-debugging-port=9222复用浏览器
            option.debugger_address = "localhost:9222"
            self._driver = webdriver.Chrome(options=option)
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

        self._driver.implicitly_wait(5)

    def close(self):
        self._driver.quit()

    def find(self, by, locator):
        return self._driver.find_element(by, locator)
