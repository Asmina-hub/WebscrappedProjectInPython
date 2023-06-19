import timeit
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Webdriver:
    def __init__(self):
        self.driver=None
    def webdriverinitialization(self):
        #start = timeit.default_timer()
        global chrome_options
        chrome_options = Options()
        #chrome_options.add_argument("--headless--")
        chrome_options.add_argument("--window-size=1920x1080")
    def OpenUrl(self,url):
        self.webdriverinitialization()
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
        self.driver.get(url)
        self.driver.maximize_window()



#webdrive=Webdriver()
#webdrive.OpenUrl("https://www.flipkart.com/")