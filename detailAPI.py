from flask import Flask, render_template, jsonify, request, Blueprint

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsearch

detailAPI = Blueprint('detail', __name__)


# 지훈님 영화 디테일 목록 순서
# 1. movie-list 페이지에서 목록 하나 클릭 시 해당 영화의 링크도 같이 url에 넘겨준다.
# ex) /movie-search?link=https://movie.naver.com/movie/bi/mi/basic.naver?code=208077
# 2. 첫번째 핑퐁
# 위에 url 에서 /movie-search api를 요청한거니까 app.py에 있는 /movie-search api를 찾는다.
# 해당 메소드에서 link를 가져온다.
# render_template을 통해 movie-search.html 파일을 넘겨줌과 동시에 link(키값)=link(밸류값) 도 같이 넘겨준다.
# 3. 두번째 핑퐁
# movie-search.html에서 우리는 크롤링한 데이터를 가져와야 하는데 링크마다 정보가 달라야 한다. 그래서 크롤링할 정보를 가져올 때 링크를 같이 넘겨준다.
# <input type="hidden" value="{{link}}" id="url_link"> 을 통해 input 값에 link데이터를 저장
# movie-search 페이지가 로딩될 때 크롤링 정보를 가져와야하니까
# $(document).ready(function (){
#             $('#movie_listBox').empty();
#             showDetailMovie();
#         })
# 이런식으로 만들어준다.
# showDetailMovie() 함수에서 크롤링할 데이터를 가져오기 위해 ajax를 사용한다.
# url: `/api/detail?link=${link}`, 로 링크를 같이 넘겨주기
# 그럼 detailAPI.py 에서 /api/detail 에 해당하는 api를 만들어준다.
# link_receive = request.args.get('link') 를 이용해서 클라이언트(ajax부분)에서 넘겨준 link를 받는다.
# 크롤링하고 doc 만들어줘서 데이터를 담아준다.
# return jsonify({'movie_detail': doc}) 을 통해 담아준 데이터를 넘긴다.
# 다시 showDetailMovie()에서 success 부분에서 받은 데이터({'movie_detail': doc}) 를 이용해서 temp_html을 만들어서 화면에 보여주면 끝!

# 영화 정보 크롤링

@detailAPI.route('/api/detail', methods=['GET'])
def listing():

    link_receive = request.args.get('link')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    response = requests.get(link_receive, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.select_one('meta[property="og:title"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']
    desc = soup.select_one('meta[property="og:description"]')['content']
    drt = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a').text
    act = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(6) > p').text
    genr = soup.select_one(
        '#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a:nth-child(1)').text

    doc = {
        'title': title,
        'image': image,
        'desc': desc,
        'drt': drt,
        'act': act,
        'genr': genr,
        'search': link_receive,
    }
    return jsonify({'movie_detail': doc})


# ## API 역할을 하는 부분
# @reviewAPI.route('/memo', methods=['POST'])
# def saving():
#     search_receive = request.form['search_give']
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     response = requests.get(search_receive, headers=headers)
#
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     title = soup.select_one('meta[property="og:title"]')['content']
#     image = soup.select_one('meta[property="og:image"]')['content']
#     desc = soup.select_one('meta[property="og:description"]')['content']
#     drt = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a').text
#     act = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(6) > p').text
#     genr = soup.select_one(
#         '#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a:nth-child(1)').text
#
#     doc = {
#         'title': title,
#         'image': image,
#         'desc': desc,
#         'drt': drt,
#         'act': act,
#         'genr': genr,
#         'search': search_receive,
#     }
#     db.movies.insert_one(doc)
#     return jsonify({'msg': '저장완'})
#
#


# review 부분
@detailAPI.route('/review', methods=['POST'])
def write_review():
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    doc = {
        'author': author_receive,
        'review': review_receive,
    }
    db.moviereview.insert_one(doc)

    return jsonify({'msg': '저장 완료'})


@detailAPI.route('/review/read', methods=['GET'])
def read_reviews():
    reviews = list(db.moviereview.find({}, {'_id': False}))
    return jsonify({'all_reviews': reviews})



# @detailAPI.route('/api/review', methods=['GET'])
# def movieReview():
#     moviereview = list(db.moviereview.find({}, {'_id:': False}))
#     return jsonify({'all_review': moviereview})
#
#
# @detailAPI.route('/api/review', methods=['POST'])
# def movieReviews():
#     author_receive = request.form['author_give']
#     review_receive = request.form['review_give']
#
#     doc = {
#         'author': author_receive,
#         'review': review_receive
#     }
#     db.moviereview.insert_one(doc)
#
#     return jsonify({'msg': '저장 완'})


# # # @app.route('/review/delete', methods=['POST'])
# # # def delete_Review():
# # #     name_receive = request.form['name_give']
# # #     db.moviereview.delete_one({'name': name_receive})
# # #     print(name_receive)
# # #     return jsonify({'msg': '삭제가 완료되었습니다'})
