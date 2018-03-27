
from framework.base_page import BasePage

class NewsHomePage(BasePage):
    #点击体育新闻入口
    sport_link = "xpath=>//*[@id='channel-all']/div/ul/li[8]/a"
    def ClickSports(self):
        self.ClickElement(self.sport_link)
        self.sleep(2)
