import requests
from flask import Blueprint, request, jsonify
from bs4 import BeautifulSoup

mymovieAPI = Blueprint('mymovie', __name__)

# API 작성하는 부분'
@mymovieAPI.route('/my-movie', methods=['POST'])
def listing():
    title = request.form['movie_title']
    url = 'https://movie.naver.com/movie/search/result.naver?query=' + title

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    data = requests.get(url, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    image = soup.select_one('#old_content > ul:nth-child(4) > li:nth-child(1) > p > a > img')
    title = soup.select_one('#old_content > ul:nth-child(4) > li:nth-child(1) > dl > dt > a').text
    print(image, title)

    return jsonify({'msg':'GET 연결되었습니다!'})
