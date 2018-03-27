
from  framework.base_page import BasePage

class SportNewsHomePage(BasePage):
    #NBA入口
    nba_link= "xpath=>//*[@id='col_nba']/div[1]/div[2]/ul[1]/li[1]/a"


    def ClickNBALink(self):
        self.ClickElement(self.nba_link)
        self.sleep(2)