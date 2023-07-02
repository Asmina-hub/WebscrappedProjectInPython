import requests

import pymongo
from flask import Flask, render_template, request
import json
from Pages.loginpage import loginpage
from Webriver.webdriver import Webdriver
from urllib.request import urlopen as uReq
app = Flask(__name__)  # initialising the flask app with the name 'app'
@app.route('/',methods=['POST','GET'])
def index():
    if request.method =='POST':
        searchstring = request.form['content'].replace(" ", "")
        try:
            dbConnect=pymongo.MongoClient("mongodb://localhost:27017/")
            db=dbConnect["webscrapper"]
            reviews=db[searchstring].find({})
            if reviews.count()>0:
                return render_template('results.html',reviews=reviews)
            else:
                webdrive = Webdriver()
                webdrive.OpenUrl("https://www.flipkart.com/")
                intialpage = loginpage(searchstring,webdrive.driver)
                intialpage.entertext()
                listofName=intialpage.searchresult()
                table = db[searchstring]
                table.insert_many(listofName)
                return render_template('results.html', reviews=listofName)
        except:
            return 'something is wrong'
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8007,debug=True) # running the app on the local machine on port 8000