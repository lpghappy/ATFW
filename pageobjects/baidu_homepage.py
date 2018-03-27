
from framework.base_page import BasePage

class HomePage(BasePage):
    input_box = "id=>kw"
    searchsubmitbtn = "xpath=>//*[@id='su']"

    #百度新闻入口
    news_link = "xpath=>//*[@id='u1']/a[1]"

    def type_search(self, text):
        self.SendKeys(self.input_box, text)

    def search_submit_btn(self):
        self.ClickElement(self.searchsubmitbtn)

    def ClickNews(self):
        self.ClickElement(self.news_link)
        self.sleep(2)
