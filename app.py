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

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.birdMovie


# HTML을 주는 부분
@app.route('/')
def main():
    path = request.path
    return render_template('index.html', path=path)

@app.route('/movie-list')
def movieList():
    path = request.path
    current_type = request.args.get('type')
    query = request.args.get('query')

    # 검색어 접근이 아닐 경우
    if query is None:
        query = 'undefined'

    return render_template('movie-list.html', path=path, current_type=current_type, query=query)

@app.route('/movie-search')
def movieSearch():
    path = request.path

    link = request.args.get('link')
    print(link)

    # 핑퐁핑퐁 순서_1번 사용할 수 있게 code 값 만들어 html로 넘겨주기
    # code값을 가져오기 위해 split로 코드만 때어와 print확인 후 넘겨 주기
    code = link.split('code=')[1]
    print(code)
    return render_template('movie-search.html', path=path, link=link, code=code)

@app.route('/my-movie')
def myMovie():
    path = request.path
    return render_template('my-movie.html', path=path)


if __name__ == '__main__':
    app.run('0.0.0.0',port=5001,debug=True)