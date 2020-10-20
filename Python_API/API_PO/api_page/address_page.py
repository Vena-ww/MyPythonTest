import requests
from MyPythonTest.Python_API.API_PO.api_page.base_api import BaseApi
from MyPythonTest.Python_API.API_PO.api_page.wework_utils import WeWorkUtils


class AddressPage(BaseApi):
    """
    通讯录管理：增删改查
    """
    def __init__(self):
        _corpsecret = "c7yr-vMycD18YcUVTb5iRkb1tPxkPOBnqz5UyymmHv8" # 通讯录页面的Secret
        utils = WeWorkUtils()
        self.token = utils.get_token(_corpsecret)

    def get_member_info(self):
        # 在URL中传入token和userID(即通讯录成员的账号)
        """base_api封装前"""
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid=HaLi"
        # return requests.get(url).json()

        """base_api封装后"""
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {"access_token": self.token, "userid": "HaLi"}
        }
        return self.send_api(data)

    def add_member(self):
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        # 接口中必须传入的参数
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {"access_token": self.token},
            # 此处的json是与原有写法requests.post(url, json=data)中的json一致的
            "json": {
                "userid": "Jerry123",
                "name": "杰瑞",
                "mobile": "12345678901",
                "department": [1]
            }
        }
        # return requests.post(url, json=data).json()
        return self.send_api(data)

    def delete_member(self):
        """base_api封装前"""
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid=Jerry123"
        # return requests.get(url).json()
        """base_api封装后"""
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid=Jerry123",
        }
        return self.send_api(data)

    def update_member(self):
        data = {
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
            "method": "post",
            "json": {
                "userid": "Jerry123",
                "name": "杰瑞123",
                "department": [7]
            }
        }
        return self.send_api(data)
