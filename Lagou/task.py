import time
import unittest,threading
import threadpool

def test_task(name):
    print(f"{threading.current_thread().name}:",name)
    time.sleep(1)

class TestTask(unittest.TestCase):
    def test01(self):
        test_task(1)

    def test02(self):
        test_task(2)

    def test03(self):
        test_task(3)

    def test04(self):
        test_task(4)

    def test05(self):
        test_task(5)

    def test06(self):
        test_task(6)

    def test07(self):
        test_task(7)

    def test08(self):
        test_task(8)

    def test09(self):
        test_task(9)

    def test10(self):
        test_task(10)


def run_testsuite(suite):
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    return result

if __name__ == '__main__':
    tl = unittest.TestLoader()
    suite = tl.loadTestsFromTestCase(TestTask)
    pool = threadpool.ThreadPool(10)
    requests = threadpool.makeRequests(run_testsuite,suite)
    for req in requests:
        pool.putRequest(req)
    pool.wait()