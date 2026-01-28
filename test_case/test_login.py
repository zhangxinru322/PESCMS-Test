import unittest
import time
import json
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from page.page_login import Pagelogin
from parameterized import parameterized

def data_case():
    json_file = os.path.join(os.path.dirname(__file__), "login_case.json")
    with open(r"D:\zhangxinru\VS\3\PESCMS\login_case.json", "r", encoding="utf-8") as f:
        test_data = json.load(f)
    return test_data
#创建测试类
class Test_login(unittest.TestCase):
    def setUp(self):
        #启动浏览器
        self.driver=webdriver.Edge()
        self.driver.maximize_window()
        #实例化，获取页面对象Pagelogin
        self.login=Pagelogin(self.driver)
        self.login.driver.get("https://team.pescms.com")
    def tearDown(self):
        self.driver.quit()
#登录测试方法
    @parameterized.expand(data_case())
    def test_login(self,username,password,expect_msg):
        #调用登陆方法
        self.login.page_login(username,password)
        time.sleep(2)
        try:
            if expect_msg == "登录成功":
                actual_title = self.driver.title
                # 精准断言标题，确保跳转到仪表盘/个人中心
                self.assertEqual("仪表盘 - PESCMS Team", actual_title,
                                 f"实际：{actual_title}")
                print("登录成功场景测试通过！")
            else:
                # 登录失败场景：断言错误提示
                msg = self.login.page_get_error_info()
                self.assertEqual( expect_msg,msg,f"错误提示不匹配。预期：{expect_msg}，实际：{msg}")
        except Exception:
            self.login.page_screenshot()
            raise