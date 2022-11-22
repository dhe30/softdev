# Daniel He, Samson Wu
# SoftDev
# K20 -- restapi
# 2022-11-21
# time spent: 1 hour

import requests
from flask import Flask, render_template

API_KEY = open('key_nasa.txt')
url = 'https://api.nasa.gov/planetary/apod'
res = requests.get(url, params={'api_key':API_KEY})
json = res.json()

date = json['date']
explanation = json['explanation']
imageurl = json['hdurl']

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html', html_date=date, html_explanation=explanation, html_image=imageurl)

if __name__ == "__main__":
    app.debug = True 
    app.run()