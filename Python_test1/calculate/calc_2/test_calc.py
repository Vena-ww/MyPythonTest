import pytest
import yaml

class GetDatas:
    with open('calc.yml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)

    # 加法的数据
    def add_data(self):
        adddatas = self.mydatas['add']['datas']
        myids = self.mydatas['add']['myids']
        return [adddatas, myids]

    def divide_data(self):
        divdatas = self.mydatas['divide']['datas']
        divids = self.mydatas['divide']['myids']
        return [divdatas, divids]

    def subtract_data(self):
        subdatas = self.mydatas['subtract']['datas']
        subids = self.mydatas['subtract']['myids']
        return [subdatas, subids]

    def multiply_data(self):
        multdatas = self.mydatas['multiply']['datas']
        multids = self.mydatas['multiply']['myids']
        return [multdatas, multids]

gd = GetDatas()

class TestCalc:
    @pytest.mark.run(order=1)
    @pytest.mark.add  # 命令行运行时可以通过这个标记选择运行哪个用例方法
    @pytest.mark.parametrize('a, b, expect', gd.add_data()[0], ids=gd.add_data()[1])
    def test_add(self, get_calc, a, b, expect):
        print("读取数据-计算两数相加")
        result = round(get_calc.add(a, b), 2)
        assert expect == result

    @pytest.mark.last
    @pytest.mark.parametrize('a, b, expect', gd.divide_data()[0], ids=gd.divide_data()[1])
    def test_divide(self, get_calc, a, b, expect):
        print("读取数据-计算两数相除")
        result = round(get_calc.divide(a, b), 2)
        assert expect == result

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a, b, expect', gd.subtract_data()[0], ids=gd.subtract_data()[1])
    def test_subtract(self, get_calc, a, b, expect):
        print("读取数据-计算两数相减")
        result = round(get_calc.subtract(a, b), 2)
        assert expect == result

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a, b, expect', gd.multiply_data()[0], ids=gd.multiply_data()[1])
    def test_multiply(self, get_calc, a, b, expect):
        print("读取数据-计算两数相乘")
        result = round(get_calc.multiply(a, b), 2)
        assert expect == result