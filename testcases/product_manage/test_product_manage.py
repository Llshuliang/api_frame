import pytest

from common.request_util import RequestUtil
#使用request实现发送接口请求
#实现统一请求封装
from common.yaml_util import read_testcases_yaml


class TestProduct:

    @pytest.mark.parametrize("caseinfo",read_testcases_yaml("/testcases/product_manage/get_token.yaml"))
    def test_get_token(self,caseinfo):
        RequestUtil().stand_cases(caseinfo)

    @pytest.mark.parametrize("caseinfo",read_testcases_yaml("/testcases/product_manage/get_tag.yaml"))
    def test_get_tag(self,caseinfo):
        RequestUtil().stand_cases(caseinfo)

    @pytest.mark.parametrize("caseinfo",read_testcases_yaml("/testcases/product_manage/create_tag.yaml"))
    def test_add_tag(self,caseinfo):
        res=RequestUtil().stand_cases(caseinfo)

    @pytest.mark.parametrize("caseinfo",read_testcases_yaml("/testcases/product_manage/file_load.yaml"))
    def test_file_load(self,caseinfo):
        res=RequestUtil().stand_cases(caseinfo)


