
import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestDemo:
    def setup(self):

        """
        # 这里是使用Options方法，打开端口，复用浏览器(只适用于Chrome浏览器)
        # 复用浏览器需要关闭所有Chrome进程，启动端口方式：chrome --remote-debugging-port=9222
        option = Options()
        option.debugger_address = 'localhost:9222'
        self.driver = webdriver.Chrome(options=option)
        """

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)  # 隐式等待，全局范围

    def teardown(self):
        self.driver.quit() # 回收driver，运行完毕后关闭窗口

    def test_case(self):
        # shelve 小型的数据库，对象持久化保存(有时效)

        """
        # 以下步骤将cookie数据存储到生成的cookieDB目录下的login_cookies文件中
        # 生成的文件也有时效性，需要定期更新
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851891057401'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'rCI0dwr7Vea9tfQoi_yeOOrrKShtXWF_8Ds7IBdQQKuiJ_0yO3ZKDxsLhINaw12LZ3pNvMyguiWGLn4pJxHmT6k0XOUctGy9g0HltoflnCcV1gMD0QoyANzuWjjFlCXYuqyhPYrMTyj1868C0_gFdq79UBIRjrqMZiEpV0Bc5m-qv3YpIf_cJ_CjR4-RAgME-2tl68NbYJGEzuHw5Wrm9iUHnCg6cjpT7KT_krB9ARI-m3FeWuhgvcadIvRcX2hSNN1wr6uuFeCtWsYJu-D8cw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851891057401'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325108157037'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'HV2RVs6hfMXoQTbqDnMf5ykdcv1xnAbbJk2s7Qb2pAk7bjA5Hco5sdXpjNfQsZwh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a941168'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '113429116871661'}, {'domain': 'work.weixin.qq.com', 'expiry': 1597917295, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '1d739gm'}, {'domain': '.qq.com', 'expiry': 1597972449, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1025667387.1597823740'}, {'domain': '.qq.com', 'expiry': 1660958049, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.2003003187.1597823740'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629359734, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '3412896832'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629360746, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1597823736'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600478052, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'a36e61490b5070fadf1adde84d2d39e5b2a234ea49653646a3f6cc46326e0519'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'OPKEABBCyr'}, {'domain': '.qq.com', 'expiry': 1597886098, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '5825735680'}]
        db = shelve.open('cookieDB/login_cookies')
        db['cookie'] = cookies # 将cookies放到db的key(cookie)下,作为cookie的值
        db.close()
        # 以上，完成cookies在文件中的存放，此时这段代码已经失去效用
        """

        # 以下，从已经生成的文件中读取cookies，然后登录页面
        db = shelve.open('cookieDB/login_cookies')
        cookies = db['cookie']   # 从cookieDB目录下的login_cookies文件中读取cookies
        db.close()
        # 打开要传入cookies的页面
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

        # 将读取的cookies信息传入到当前打开的页面中
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')  # 删除expiry(Cookie有效终止日期，出现浮点数时影响运行)
            self.driver.add_cookie(cookie)  # 传送cookie数据

        # 获取cookies后重新进入页面(当前页面自动刷新)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # 定位到导入通讯录按钮并点击
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        # send_keys()上传文件，文件路径中的\会引起转义的问题，所有前面加r保持原始值，或替换为\\或/
        self.driver.find_element(By.ID, 'js_upload_file_input').send_keys(r'D:\Download\upload_data.xlsx')
        # driver.find_element().text中的text是指定位到的元素的文本
        # 断言上传成功的文件是否正确
        assert 'upload_data.xlsx' == self.driver.find_element(By.ID, 'upload_file_name').text



