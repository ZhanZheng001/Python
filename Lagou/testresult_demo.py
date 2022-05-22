import unittest
import HTMLTestRunner_PY3

if __name__ == '__main__':
    t1 = unittest.TestLoader()
    suite = t1.discover("./","task.py")
    with open('./result.html',mode='wb')as f:
        runner = HTMLTestRunner_PY3.HTMLTestRunner(f,verbosity=2,title="结果展示")
        runner.run(suite)

