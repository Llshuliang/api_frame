# import re
#
# import pytest
# import requests
# from common.request_util import RequestUtil
# from common.yaml_util import yaml_extract_write,yaml_extract_read
#
#
# class TestUser:
#     csrf_token=""
#     @pytest.mark.run(order=1)
#     def test_user(self):
#         print("访问phpwind论坛首页接口")
#         url="http://47.107.116.139/phpwind/"
#         method="get"
#         res=RequestUtil().Request_util(url=url,method=method)
#         TestUser.csrf_token=re.search('name="csrf_token" value="(.*?)"',res.text).group(1)
#         print(TestUser.csrf_token)
#         yaml_extract_write({"csrf_token": TestUser.csrf_token})
#         # TestUser.cookie=res.cookies
#     @pytest.mark.run(order=2)
#     def test_login(self):
#         print("登录接口")
#         url="http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
#         method="post"
#         headers={
#             "Accept":"application/json, text/javascript, /; q=0.01",
#             "X-Requested-With":"XMLHttpRequest"
#         }
#         data={
#             "username":"admin",
#             "password":"msxy",
#             "csrf_token": yaml_extract_read("csrf_token"),
#             "backurl":"http://47.107.116.139/phpwind/",
#             "invite": ""
#         }
#         res=RequestUtil().Request_util(url=url,method=method,headers=headers,data=data)
