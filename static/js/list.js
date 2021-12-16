$(document).ready(function (){
    // 페이지 로딩 시 영화목록 초기화
    $('.movie-listBox').empty();
    let type = $('#movie-type').val();  // 타입 가져오기
    let query = $('#query').val();  // 검색어 가져오기

    if (query === 'undefined') {
        // 검색어로 접근 아닐경우 : 영화 리스트 불러오기
        showList(type);
    } else {
        // 검색어로 접근일 경우 : 검색 목록 불러오기
        showSearchList(query);
    }
})

function showSearchList(query) {

    $.ajax({
        type: 'GET',
        url: `/api/search-list?query=${query}`,
        data: {},
        success: function (response) {
            let movies = response['items'];

            for (let i = 0; i < movies.length; i++) {
                let movie = movies[i];

                let title = movie['title'];
                let img = movie['image'];
                let actor = movie['actor'];
                let director = movie['director'];
                let link = movie['link'];

                let temp_html =
                    `<div class="movie-list">
                        <a class="list-img" href="/movie-search?link=${link}"><img src="${img}"></a>
                        <div class="list-cont">
                            <div class="movie-name">
                                <span class="movie-age">15</span><span class="movie-tit">${title}</span>
                            </div>
                            <div class="director">
                                <span class="title">감독</span><span class="text">${director}</span>
                            </div>
                            <div class="actor">
                                <span class="title">출연</span><span class="text">${actor}</span>
                            </div>
                        </div>
                        <button class="list-like">
                            <i class="fas fa-heart"></i>
                            <span>1</span>
                        </button>
                    </div>`

            $('.movie-listBox').append(temp_html)

            }


        }
    })
}

function showList(type) {
    let menuType = (type)

    $.ajax({
        type: "GET",
        url: `/list?type=${menuType}`,
        data: {},
        success: function (response) { // 성공하면
             console.log(response["movie_list"]);
            let current = response["movie_list"]

            for (let i = 0; current.length; i++){
                let title = current[i]['title']
                let img = current[i]['img']
                let kinds = current[i]['kinds']
                let director = current[i]['director']
                let link = current[i]['link']

                let temp_html =
                    `<div class="movie-list">
                        <a class="list-img" href="/movie-search?link=${link}"><img src="${img}"></a>
                        <div class="list-cont">
                            <div class="movie-name">
                                <span class="movie-age">15</span><span class="movie-tit">${title}</span>
                            </div>
                            <div class="summary">
                                <span class="title">개요</span><span class="text">${kinds}</span>
                            </div>
                            <div class="director">
                                <span class="title">감독</span><span class="text">${director}</span>
                            </div>
                            <div class="actor">
                                <span class="title">출연</span><span class="text">
                                배우없는 영화있어!! 크롤링 안돼! 나이제한도!! none나와서 못했어!!! 으악ㄱㄱ</span>
                            </div>
                            <div class="contents">
                                <span class="title">줄거리</span>
                                <p class="text"></p>
                            </div>
                        </div>
                        <button class="list-like">
                            <i class="fas fa-heart"></i>
                            <span>1</span>
                        </button>
                    </div>`
            $('.movie-listBox').append(temp_html)
            }
        }
    })
}