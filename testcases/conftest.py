#所有用例执行之前执行
#使用fixture固件
import pytest
from common.yaml_util import yaml_extract_clear

@pytest.fixture(scope="session",autouse=True)
def begin():
    yaml_extract_clear()
    print("用例执行之前：")
    yield
    print("用例执行之后")


#所有用例执行之后执行