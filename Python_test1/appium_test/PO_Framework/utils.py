import yaml


class Utils:
    @classmethod
    def load_file(cls, path):
        with open(path, encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
            params = yaml_data['params']  # params是一个列表中嵌套多个字典
            keys = set()   # set() 函数创建一个无序不重复元素的集合
            values = []    # 设置values为列表形式

            # 判断params是否是列表形式，此处返回值为True
            if isinstance(params, list):
                for row in params:   # 遍历取出列表中的每个字典
                    if isinstance(row, dict):   # 判断row是否是字典形式，此处返回值为True
                        for key in row.keys():  # 遍历字典row中的key
                            keys.add(key)   # 取出列表中所有的key,如果key值相同，则不会被添加到keys中
                            values.append(list(row.values())[0])  # 取出字典row中所有的value(list形式)添加到values中
            var_name = ','.join(keys)   # 获取的字典形式的keys值使用join()以逗号连接多个字符串
            res = {'keys': var_name, 'values': values}
            print(res)
            return res
