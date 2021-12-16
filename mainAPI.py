from flask import Blueprint, request, jsonify

import requests
from bs4 import BeautifulSoup

mainAPI = Blueprint('main', __name__)

# API 작성하는 부분
@mainAPI.route('/api/movies')
def movies():
    movie_list = get_movies('https://movie.naver.com/movie/running/current.naver')

    return jsonify({'result':'success', 'movie_list':movie_list})


@mainAPI.route('/api/rank')
def rank():
    movie_list = get_movies('https://movie.naver.com/movie/running/current.naver?view=list&tab=normal&order=point')

    return jsonify({'result':'success', 'movie_list':movie_list})


def get_headers(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    return soup


def get_movies(url):
    # bs4 headers 등록
    soup = get_headers(url)

    # 영화 데이터 딕셔너리 넣어줄 리스트 초기화
    movie_list = []

    # 가져올 영화 갯수
    count = 5

    # link 앞에 공통으로 붙일 url
    naver_url = 'https://movie.naver.com'

    # 스크래핑 코드
    movies = soup.find('ul', class_='lst_detail_t1').find_all('li')

    for index, movie in enumerate(movies):
        title = movie.select_one('dt.tit > a').text
        link = naver_url + movie.select_one('dt.tit > a')['href']
        img = movie.select_one('img')['src']

        # 딕셔너리에 담아주기
        dic = {'title': title, 'img': img, 'link': link}

        # 리스트에 dic 추가
        movie_list.append(dic)

        # 영화 보여줄 갯수 만큼만 반복문 돌기
        if index + 1 == count:
            break

    return movie_list

