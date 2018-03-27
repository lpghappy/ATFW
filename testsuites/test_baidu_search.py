
import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.logger import Logger
from pageobjects.baidu_homepage import HomePage

logger = Logger(logger="BaiduSearch").getlog()


class BaiduSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        logger.info("Now, Close and quit the browser.")
        cls.driver.quit()

    def test_baidu_search1(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        logger.info("test_baidu_search1 starting...")
        homepage = HomePage(self.driver)
        homepage.type_search("selenium")#调用页面对象中的方法
        homepage.search_submit_btn()#调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        homepage.GetWindowImg()# 调用基类截图方法
        try:
            assert "selenium" in homepage.GetPageTitle() # 调用页面对象继承基类中的获取页面标题方法
            logger.info("Test Pass.")
        except Exception as e:
            logger.info("Test Fail.", format(e))
        logger.info("test_baidu_search1 end.")

    def test_baidu_search2(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        logger.info("test_baidu_search2 starting...")
        homepage = HomePage(self.driver)
        homepage.type_search("python")#调用页面对象中的方法
        homepage.search_submit_btn()#调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        homepage.GetWindowImg()# 调用基类截图方法
        try:
            assert "python" in homepage.GetPageTitle()  # 调用页面对象继承基类中的获取页面标题方法
            logger.info("Test Pass.")
        except Exception as e:
            logger.info("Test Fail.", format(e))
        logger.info("test_baidu_search2 end.")

# if __name__ == "__main__":
#     unittest.main()
