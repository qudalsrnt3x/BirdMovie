$(document).ready(function () {
    // 현재 상영작 보여주기
    showCurrentMovies();

    // 영화 순위 보여주기
    showMovieRank();
})

function showCurrentMovies() {
    $.ajax({
        url: '/api/movies',
        type: 'GET',
        data: {},
        success: function (response) {
            if (response['result'] === 'success') {
                let movies = response['movie_list']

                for (let i = 0; i < movies.length; i++) {
                    let movie = movies[i]

                    let title = movie['title'];
                    let img = movie['img'];
                    let link = movie['link'];

                    let temp_html = `<a class="card" href="{{url_for('movieList')}}">
                                        <img src="${img}" alt="${title}" title="${title}">
                                        <sapn>${textLengthOverCut(title)}</sapn>
                                    </a>`;

                    $('#movie-box').append(temp_html);
                }
            }
        }
    })
}

function showMovieRank() {
    $.ajax({
        url: '/api/rank',
        type: 'GET',
        data: {},
        success: function (response) {
            if (response['result'] === 'success') {
                let movies = response['movie_list']

                for (let i = 0; i < movies.length; i++) {
                    let movie = movies[i]

                    let title = movie['title'];
                    let img = movie['img'];
                    let link = movie['link'];

                    let temp_html = `<a class="card" href="{{url_for('movieList')}}">
                                        <img src="${img}" alt="${title}" title="${title}">
                                        <sapn>${textLengthOverCut(title)}</sapn>
                                    </a>`;

                    $('#rank_box').append(temp_html);
                }
            }
        }
    })
}

/*  @returns 결과값
 * <br/>
 * <br/>
 * 특정 글자수가 넘어가면 넘어가는 글자는 자르고 마지막에 대체문자 처리<br/>
 * ex) 가나다라마바사 -> textLengthOverCut('가나다라마바사', '5', '...') : 가나다라마...<br/>
*/
function textLengthOverCut(txt, len, lastTxt) {
    if (len == "" || len == null) { // 기본값
        len = 10;
    }
    if (lastTxt == "" || lastTxt == null) { // 기본값
        lastTxt = "...";
    }
    if (txt.length > len) {
        txt = txt.substr(0, len) + lastTxt;
    }
    return txt;
}

// 검색어 부분
function goListBySearch(type) {
    // 검색어 받아오기
    let query = $('#search-box').val();

    if (query === '') {
        alert('검색어를 입력해주세요.');
        $('#search-box').focus();
        return;
    }

    // movie-list 페이지로 이동 시 query, type 같이 보내주기
    location.href = `/movie-list?query=${query}&type=${type}`;
}

// 리스트페이지로 이동
function goList(type) {

    location.href = `/movie-list?type=${type}`;
}