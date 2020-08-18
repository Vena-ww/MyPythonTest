import pytest
import yaml
from MyPythonTest.Python_test1.calculate.calc_1.calculate import Calculator


# 数据驱动  从yaml文件读取测试数据
def get_data():
    with open('calc.yml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        myids = mydatas['add']['myids']
    return [adddatas, myids]


class TestCalc:
    # 类级别的方法，只在类中的方法执行前后被调用一次
    def setup_class(self):
        print("类中的方法执行前调用一次")
        self.calc = Calculator()

    def teardown_class(self):
        print("在类中的方法执行后调用一次")

    def setup(self):
        print("\n开始计算")
        self.calc = Calculator()

    def teardown(self):
        print("\n计算结束\n")

    # 数据驱动，从yaml文件读取参数
    @pytest.mark.add
    @pytest.mark.parametrize('a, b, expect', get_data()[0], ids=get_data()[1])
    def test_add(self, a, b, expect):
        print("读取数据-计算两数相加")
        result = self.calc.add(a, b)
        assert expect == result

    # 参数化用例数据-----加法
    @pytest.mark.parametrize('a, b, expect', [
        (0.1, 0.1, 0.2),
        (20, 10, 30)
    ], ids=['小数', '整数'])
    def test_add_para(self, a, b, expect):
        print('参数化两数相加')
        result = round(self.calc.add(a, b), 2)
        assert expect == result

    # 参数化用例数据-----除法
    @pytest.mark.div
    @pytest.mark.parametrize('a, b, expect', [
        (0, 0, 0),
        (0, 2, 0),
        (20, 10, 2),
        (0.5, 0.2, 0.25),
        (-2, -2, 1)
    ], ids=['零零相除', '零做被除数', '整数相除', '小数相除', '负数相除'])
    def test_div(self, a, b, expect):
        print('测试相除')
        result = round(self.calc.div(a, b), 2)
        assert expect == result

