import  time
import pytest
import requests
import allure
@allure.epic("接口自动化测试项目")
@allure.feature("用户管理模块")

class TestApi:
    @allure.story("码尚教育1")
    @allure.title("登陆成功")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_01_mashang(self):
        print("码尚教育1")
        requests.get()
        requests.post()
        requests.put()
        requests.delete()
        requests.request()
    # @allure.story("码尚教育2")
    # @allure.title("登陆成功")
    # def test_02_mashang(self):
    #     print("码尚教育2")



