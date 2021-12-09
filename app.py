from flask import Flask, render_template, jsonify, request
import json
app = Flask(__name__)

# 각 기능API 임포트
from mainAPI import mainAPI
from listAPI import listAPI
from detailAPI import detailAPI
from mymovieAPI import mymovieAPI

app.register_blueprint(mainAPI)
app.register_blueprint(listAPI)
app.register_blueprint(detailAPI)
app.register_blueprint(mymovieAPI)

import requests
from bs4 import BeautifulSoup


from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.birdMovie


# HTML을 주는 부분
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/footers')
def footer():
    return render_template('layout/footer.html')

@app.route('/movie-List')
def movieList():
    return render_template('movie-list.html')

@app.route('/movie-Search')
def movieSearch():
    return render_template('movie-search.html')

@app.route('/my-movie')
def myMovie():
    return render_template('my-movie.html')


if __name__ == '__main__':
    app.run('0.0.0.0',port=5001,debug=True)