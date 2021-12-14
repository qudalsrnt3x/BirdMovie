from flask import Blueprint, request, jsonify

listAPI = Blueprint('list', __name__)

# API 작성하는 부분
@listAPI.route('/list', methods=['GET'])
def makeList():
    type_receive = request.args.get('type')
    # return jsonify({'msg': type_receive})
    movie_list = []

    # 영화 가져올 갯수
    count = 10

    if type_receive == 'current':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get('https://movie.naver.com/movie/running/current.naver', headers=headers)
        html = data.text
        soup = BeautifulSoup(html, 'html.parser')

        movies = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')

        for index, movie in enumerate(movies):
            img = movie.select_one('.thumb> a > img')['src']
            title = movie.select_one('.tit > a').text
            kinds = movie.select_one('.info_txt1 > dd > span > a').text
            director = movie.select_one('.info_txt1 > dd:nth-child(4) > span > a').text

            # 딕셔너리에 담기
            dic = {'img': img,
                   'title': title,
                   'kinds': kinds,
                   'director': director}

            # DB에 dic추가
            movie_list.append(dic)
            #print

            if index + 1 == count:
                break


        return jsonify({'movie_list':movie_list})
        #DB저장하고나면 msg가 안가나??? 왜 console.log에 응답안감?? ㅡㅡ

    else:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get('https://movie.naver.com/movie/running/current.naver?view=list&tab=normal&order=point', headers=headers)
        html = data.text
        soup = BeautifulSoup(html, 'html.parser')

        movies = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')

        for index, movie in enumerate(movies):
            img = movie.select_one('.thumb> a > img')['src']
            title = movie.select_one('.tit > a').text
            kinds = movie.select_one('.info_txt1 > dd > span > a').text
            director = movie.select_one('.info_txt1 > dd:nth-child(4) > span > a').text

            # 딕셔너리에 담기
            dic = {'img': img,
                   'title': title,
                   'kinds': kinds,
                   'director': director}

            # DB에 dic추가
            movie_list.append(dic)
            print(movie_list)

            if index + 1 == count:
                break

        return jsonify({'movie_list': movie_list})
