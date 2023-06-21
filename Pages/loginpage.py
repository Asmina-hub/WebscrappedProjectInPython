import json
import time

from pip._vendor.rich import table
from selenium.webdriver.common.by import By

from Object_Repository.WebScrapperObjRepo import WebdriverObjRepo
from Webriver.webdriver import Webdriver
loginpageobj=WebdriverObjRepo()
webdrive=Webdriver()
class loginpage(WebdriverObjRepo):
    global jsonFile
    jsonFile= open("data.json", "w")
    def __init__(self, value):
        self.value=value
        self.driver=webdrive.driver
        self.closebutton=loginpageobj.closebutton
        self.textbox=loginpageobj.textbox
        self.search=loginpageobj.search

    def entertext(self):
        input_element = self.driver.find_element(By.CSS_SELECTOR,self.closebutton)
        input_element.click()
        time.sleep(5)
        text_element = self.driver.find_element(By.CSS_SELECTOR,self.textbox).send_keys(self.value)
        search_button = self.driver.find_element(By.CSS_SELECTOR, self.search)
        search_button.click()
    def clickonpagenumber(self,i):
        print(loginpageobj.number(str(i)))
        self.driver.find_element(By.XPATH, loginpageobj.number(str(i))).click()

    def searchresult(self):
        time.sleep(5)
        pagenumberstring = self.driver.find_element(By.XPATH, loginpageobj.finalPageNumber).text
        totalpagenumber= pagenumberstring.split(" ")[3]
        for i in range(1,2):
            time.sleep(5)
            self.clickonpagenumber(1)
            for j in range(1,25):
                time.sleep(2)
                self.driver.find_element(By.XPATH, loginpageobj.clickontheitem(str(j))).click()
                time.sleep(2)
                self.driver.switch_to.window(self.driver.window_handles[1])
                time.sleep(2)
                mydict=self.getReview()
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])

        jsonFile.close()
        return mydict


    def getReview(self):
        productname = self.driver.find_element(By.XPATH, loginpageobj.productname).text
        self.driver.find_element(By.XPATH,loginpageobj.reviewtext).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,loginpageobj.reviewclick).click()
        time.sleep(3)
        for i in range(1,11):
            individualprorating = self.driver.find_element(By.XPATH, loginpageobj.individualrating(str(i))).text
            individualprotitle = self.driver.find_element(By.XPATH, loginpageobj.individualreviewtitle(str(i))).text
            individualprosummary = self.driver.find_element(By.XPATH, loginpageobj.individualreviewcomments(str(i))).text
            mydict = {"Product": productname, "Rating": individualprorating, "CommentHead": individualprotitle,
                      "Comment": individualprosummary}
            jsonString = json.dumps(mydict)
            jsonFile.write(jsonString)
        return jsonString

    def driverclose(self):
        self.driver.close()











