import unittest
from BeautifulReport import BeautifulReport
import os
import time

# 测试报告的存放路径
report_path = "./report"
# 测试报告的标题
report_title = "PESCMS测试报告"
# 测试报告的描述
report_desc = "对PESCMS登录功能进行测试"

# 判断是否有目录report，有则写入，没有则创建
if not os.path.exists(report_path):
    os.mkdir(report_path)

# 指定用例的加载路径（修改为test_case目录）
case_path = os.path.join(os.path.dirname(__file__), 'test_case')

# 模糊匹配
suite = unittest.defaultTestLoader.discover(start_dir=case_path, pattern="test_login.py")

result = BeautifulReport(suite)
result.report(
    filename="测试报告",
    description=report_desc,
    report_dir=report_path
)