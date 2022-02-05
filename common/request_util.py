import json
import random
import re

import jsonpath
import requests

from common.yaml_util import yaml_extract_write
from redload.red_load import RedLoad


class RequestUtil:
    session = requests.session()

    def replace_cases(self, value):
        # 保存数据类型
        # print(value)
        data_type = type(value)
        # 判断数据类型
        if isinstance(value, dict) or isinstance(value, list):
            str_data = json.dumps(value)
        else:
            str_data = str(value)

        if "${" in str_data and "}" in str_data:
            begin_index = str_data.index("${")
            end_index = str_data.index("}")
            old_value = str_data[begin_index:end_index + 1]
            func_name = old_value[2:old_value.index("(")]
            ars_name = old_value[old_value.index("(") + 1:old_value.index(")")]
            if ars_name != "":
                ars_name_new = ars_name.split(",")
                new_value = getattr(RedLoad(), func_name)(*ars_name_new)
            else:
                new_value = getattr(RedLoad(), func_name)()
            str_data = str_data.replace(old_value, str(new_value))
            # 恢复数据类型
            if isinstance(value, dict) or isinstance(value, list):
                value = json.loads(str_data)
            else:
                value = data_type(str_data)
        return value

        # 使用热加载？？？

    # 标准化用例判断，判断yaml用例格式符合规范的话，就进行数据提取，否则进行报错；
    # 判断用例中是否有需要提取的值，如果需要进行提取
    def stand_cases(self, caseinfo):
        # try:
            print(caseinfo)
            if "name" in caseinfo.keys() and "request" in caseinfo.keys() and "validate" in caseinfo.keys():
                if "method" in caseinfo["request"] and "url" in caseinfo["request"]:
                    method = caseinfo["request"].pop("method")
                    url = caseinfo["request"].pop("url")
                    data = caseinfo["request"]
                    res = self.request_all(method=method, url=url, **data)
                    return_value = res.json()
                    return_text = res.text
                    if "extract" in caseinfo.keys():
                        for key, value in caseinfo["extract"].items():
                            print(key, value)
                            if "(.*?)" in value or "(.+?)" in value:
                                js_value = re.search(value, return_text).group(1)
                                if js_value:
                                    extract_value = {key: js_value}
                                    yaml_extract_write(extract_value)
                            else:
                                js_value = jsonpath.jsonpath(return_value, value)
                                print(js_value[0])
                                if js_value:
                                    extract_value = {key: js_value[0]}
                                    yaml_extract_write(extract_value)
                    sj_value = res.text
                    return_code = res.status_code
                    self.assert_result(caseinfo["validate"], sj_value, return_code)
                    return res
                else:
                    print("请求参数缺少必须的method、url，请检查yaml用例")

            else:
                print("yaml用例不符合规范，缺少必须的键'name', 'request','validate'，请检查yaml用例")
        # except Exception as e:
        #     print("读取标准化stand_cases方法异常")


    def request_all(self, method, url, **kwargs):
        # method=method.lower()
        # 请求里面的数据判断是否存在替换呢？
        # self.replace_cases(kwargs)
        method = str(method).lower()
        url = self.replace_cases(url)
        for key, value in kwargs.items():
            if key in ["params", "data", "json", "headers"]:
                kwargs[key] = self.replace_cases(value)
            elif key == "files":
                for file_key, file_value in value.items():
                    # print(file_key,file_value)
                    value[file_key] = open(file_value, "rb")
                    # print(value[file_key])
        res = RequestUtil.session.request(url=url, method=method, **kwargs)
        print(res.text)
        return res


    def assert_result(self, yq_value, sj_value, return_code):
        try:
            flag_all=0
            for yq_val in yq_value:
                # print(value)
                for key, val_yq in yq_val.items():
                    # print(key,yq_val)
                    if key == "equals":
                        # 相等断言
                        flag=self.equals_assert(return_code, sj_value, val_yq)
                        flag_all = flag_all + flag
                        print("************")
                        print(flag_all)
                    elif key == "contains":
                        # 包含断言
                        flag = self.contains_assert(sj_value, val_yq)
                        flag_all = flag_all + flag
                    else:
                        print("此框架不支持此断言方式")
            print("-------------"+flag_all)
            assert  flag_all==0

        except Exception as e:
            print(f"读取assert_result断言方法异常")

    def equals_assert(self, return_code, sj_value, yq_value):
        flag = 0
        for assert_key, assert_value in yq_value.items():
            if assert_key == "status_code":
                if assert_value != return_code:
                    print("断言失败，返回的状态码不等于%s" % (assert_value))
                    flag = flag + 1
            else:
                lists = jsonpath.jsonpath(json.loads(sj_value), '$..%s' % assert_key)
                print(sj_value)
                print(f"lists:{lists}")
                if lists:
                    if assert_value not in lists:
                        print("断言失败：" + str(assert_key) + "不等于" + str(assert_value))
                    flag = flag + 1
                else:
                    print("断言失败，返回的结果中不存在" + str(assert_value))
                    flag = flag + 1
        return flag


    def contains_assert(self, sj_value, yq_value):
        flag = 0
        if str(yq_value) not in str(sj_value):
            print("断言失败：返回结果中不包含" + str(yq_value))
            flag = flag + 1
        return flag
