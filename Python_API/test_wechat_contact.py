import requests

corpid = 'wwc72ee4311e0af881'  # 企业ID
corpsecret = 'c7yr-vMycD18YcUVTb5iRkb1tPxkPOBnqz5UyymmHv8'   # 通讯录页面的Secret
# 获取token信息
def get_token():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
    result = requests.get(url).json()
    return result['access_token']   # 取出token信息以便其他接口调用

# 读取成员信息
def test_get():
    token = get_token()
    # 在URL中传入token和userID(即通讯录成员的账号)
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=Jerry123"
    print(requests.get(url).json())

# 创建成员
def test_add():
    token = get_token()
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    # 接口中必须传入的参数
    data = {
        "userid": "Jerry123",
        "name": "杰瑞",
        "mobile": "12345678901",
        "department": [1]
    }
    print(requests.post(url, json=data).json())

# 更新成员信息
def test_update():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}"
    data = {
        "userid": "Jerry123",
        "name": "杰瑞123",
        "department": [7]
    }
    print(requests.post(url, json=data).json())

# 删除成员
def test_delete():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=Jerry123"
    print(requests.get(url).json())

# 创建部门
def test_department_add():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={get_token()}"
    data = {
        "name": "子部门",
        "parentid": 2
    }
    print(requests.post(url, json=data).json())

# 更新部门
def test_department_update():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={get_token()}"
    data = {
        "id": 8,
        "name": "子部门_2"
    }
    print(requests.post(url, json=data).json())

# 删除部门
def test_department_delete():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={get_token()}&id=7"
    res = requests.get(url).json()
    assert 0 == res["errcode"]

# 获取部门列表--API中规定：获取指定id的部门及其子部门，若不填id则默认获取全量组织架构
def test_get_department():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={get_token()}&id=2"
    print(requests.get(url).json())
