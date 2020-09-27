import json

import requests


class BaseApi:
    """
    api的抽象类
    """
    def send_api(self, data: dict):
        """
        发送api
        """
        print(json.dumps(data, indent=2))
        return requests.request(**data).json()