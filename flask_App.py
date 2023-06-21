import requests

import pymongo
from flask import Flask, render_template, request

from Pages.loginpage import loginpage
from Webriver.webdriver import Webdriver

app = Flask(__name__)  # initialising the flask app with the name 'app'
@app.route('/',methods=['POST','GET'])
def methodStart():
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
                intialpage = loginpage(searchstring)
                intialpage.entertext()
                mydict=intialpage.searchresult()
                table = db[searchstring]
                reviews = []
                x = table.insert_many(mydict)  # insertig the dictionary containing the rview comments to the collection
                reviews.append(mydict)
                return render_template('results.html', reviews=reviews)
        except:
            return 'something is wrong'
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(port=49675,debug=True) # running the app on the local machine on port 8000