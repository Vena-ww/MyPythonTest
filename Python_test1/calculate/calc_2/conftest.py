from typing import List
import pytest
from MyPythonTest.Python_test1.calculate.calc_2.calculate import Calculator


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

# test_calc.py文件的fixture方法
@pytest.fixture(scope='module')
def get_calc():
    print('开始计算')
    calc = Calculator()
    yield calc
    print('结束计算')

# 获取get_data()方法的返回值，作为参数传入fixture方法
# @pytest.fixture(params=get_data()[0], ids=get_data()[1])
# def used_fixture(request):
#     return request.param
