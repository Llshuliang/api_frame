import os

import yaml


def getcwd():
    return os.getcwd()


# 全局变量关联写入
def yaml_extract_write(data):
    with open(getcwd() + "/extract.yaml", mode="a", encoding="utf-8") as f:
        result = yaml.dump(data=data, stream=f, allow_unicode=True)
    # return result



# 全局变量清除
def yaml_extract_clear():
    with open(getcwd() + "/extract.yaml", mode="w", encoding="utf-8") as f:
        result = f.truncate()

#读取测试用例
def read_testcases_yaml(path):
    with open(getcwd()+path,mode="r",encoding='utf-8') as f:
        data=yaml.full_load(f)
    return data