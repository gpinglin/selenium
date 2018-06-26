# coding = UTF-8
import HTMLTestRunner
import os
import unittest
import time

# 设置报告文件保存路径


report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
filename = report_path + now + "HTMLtemplate.html"
fp = open(filename, "wb")

# 构建suite
suite = unittest.TestLoader().discover("testcase")

if __name__ == '__main__':
   runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"知乎项目测试报告", description=u"用例测试情况")
   # 开始执行测试套件
   runner.run(suite)
   fp.close()