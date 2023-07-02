from selenium.webdriver.common.by import By
from Webriver.webdriver import Webdriver

class WebdriverObjRepo(Webdriver):
         textbox = 'input[placeholder="Search for products, brands and more"]'
         closebutton ='button[class="_2KpZ6l _2doB4z"]'
         search='button[type="submit"]'
         finalPageNumber='//span[contains(text(),"Page")]'
         reviewtext='(//span[contains(text(),"Review")])[1]'
         productname='//span[@class="B_NuCI"]'
         rating='//div[@class="_2d4LTz"]'
         reviewclick='//span[contains(text(),"reviews")]'
         def individualrating(self,i):
             eachrating='(//div[contains(@class,"_3LWZlK _")])['+i+']'
             return eachrating
         def individualreviewtitle(self,i):
             eachrating='(//p[@class="_2-N8zT"])['+i+']'
             return eachrating
         def individualreviewcomments(self,i):
             eachrating='(//div[@class="t-ZTKy"])['+i+']'
             return eachrating
         def clickontheitem(self,i):
             eachphonexpath = '(//div[@class="_4rR01T"])['+i+']'
             return eachphonexpath
         def number(self,i):
            numberbutton='//a[text()='+i+']'
            return numberbutton





