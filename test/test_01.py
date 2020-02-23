import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config ,DATA_PATH,REPORT_PATH# DRIVER_PATH,
from utils.log import logger
from utils.file_reader import ExcelReader
from utils.HTMLTestRunner_PY3 import HTMLTestRunner


class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')


    def sub_setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.URL)

    def sub_tearDown(self):
        self.driver.quit()

    def test_search(self):
        #从表格中读取数据
        datas = ExcelReader(self.excel).data

        for d in datas:
            with self.subTest(data = d):
                self.sub_setUp()
                self.driver.find_element(*self.locator_kw).send_keys(d['search'])
                self.driver.find_element(*self.locator_su).click()
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()


if __name__ == '__main__':
    report_file = REPORT_PATH + '\\report.html'

    testsuite = unittest.TestSuite()

    #把测试用例集传入到testsuite中
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestBaiDu))

    with open(report_file,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='测试报告测试',description='修改html报告')
        #runner.run(TestBaiDu('test_search'))
        runner.run(testsuite)


