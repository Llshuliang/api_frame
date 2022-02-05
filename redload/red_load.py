import random

import yaml

from common.yaml_util import  getcwd


class RedLoad:
# 全局变量读取
  def yaml_extract_read(self,key):
     with open(getcwd() + "/extract.yaml", mode="r", encoding="utf-8") as f:
         result = yaml.full_load(f)
     return result[key]


  def random_sz(self,min,max):
      print(f"最小值：{min}，最大值{max}")
      data=random.randint(int(min),int(max))
      print(data)
      return str(data)

#
# if __name__=="__main__":
#     RedLoad().random_sz(1000,9999)