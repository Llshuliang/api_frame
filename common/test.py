
import yaml
#写入到yaml文件
def write_extract_yaml(data):
    with open("path",mode="a",encoding="utf-8") as f:
        result=yaml.dump(data,stream=f,allow_unicode=True)
    return result

#读取yaml文件
def reade_extract_yaml(key):
    with open("path",mode='r',encoding="utf-8") as f:
        result=yaml.full_load(f)
    return  result


#清除yaml文件
def clear_extrat_yaml():
    with open("path",mode='w',encoding="utf-8") as f:
          f.truncate()