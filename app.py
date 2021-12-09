from flask import Flask, render_template, jsonify, request
import json
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup


from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.birdMovie


# HTML을 주는 부분
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/movie-List')
def movieList():
    return render_template('movie-list.html')

@app.route('/movie-Search')
def movieSearch():
    return render_template('movie-search.html')

@app.route('/my-movie')
def myMovie():
    return render_template('my-movie.html')
#


## API 부분

@app.route('/memo', methods=['GET'])
def listing():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg':'GET 연결되었습니다!'})


@app.route('/memo', methods=['POST'])
def saving():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg':'POST 연결되었습니다!'})


if __name__ == '__main__':
    app.run('0.0.0.0',port=5001,debug=True)