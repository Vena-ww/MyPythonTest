import requests

from MyPythonTest.Python_API.API_PO.api_page.base_api import BaseApi


class WeWorkUtils(BaseApi):
    # corpid---企业ID
    # corpsecret---页面的Secret
    def get_token(self, corpsecret, corpid='wwc72ee4311e0af881'):
        """base_api封装前"""
        # url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
        # result = requests.get(url).json()

        """base_api封装后"""
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {"corpid": corpid, "corpsecret": corpsecret}
        }
        result = self.send_api(data)
        return result['access_token']  # 取出token信息以便其他接口调用
