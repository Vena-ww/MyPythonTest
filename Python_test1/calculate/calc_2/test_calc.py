import pytest
import yaml


class TestCalc:
    # get_datas是个列表
    @pytest.mark.add
    def test_add(self, get_calc, used_fixture):
        print("读取数据-计算两数相加")
        result = get_calc.add(used_fixture[0], used_fixture[1])
        assert used_fixture[2] == result

