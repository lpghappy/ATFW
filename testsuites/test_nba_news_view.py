import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
from pageobjects.baidu_news_home import NewsHomePage
from pageobjects.news_sport_home import SportNewsHomePage
from framework.logger import Logger

logger = Logger(logger="TestNBANewsView").getlog()

class ViewNBANews(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_view_nba_views(self):

        logger.info("test_view_nba_views is starting...")

        # 初始化百度首页，并点击新闻链接
        baiduhome = HomePage(self.driver)
        # baiduhome.ClickNews()
        news_link = "//*[@id='u1']/a[1]"
        self.driver.find_element_by_xpath(news_link).click()

        # 初始化一个百度新闻主页对象，点击体育
        newshome = NewsHomePage(self.driver)
        # newshome.ClickSports()
        sport_link = "//*[@id='channel-all']/div/ul/li[8]/a"
        self.driver.find_element_by_xpath(sport_link).click()

        # 初始化一个体育新闻主页，点击NBA
        sportnewhome = SportNewsHomePage(self.driver)
        # sportnewhome.ClickNBALink()
        nba_link = "//*[@id='col_nba']/div[1]/div[2]/ul[1]/li[1]/a"
        self.driver.find_element_by_xpath(nba_link).click()
        sportnewhome.GetWindowImg()

        logger.info("test_view_nba_views is end.")


# if __name__ == '__main__':
#     unittest.main()