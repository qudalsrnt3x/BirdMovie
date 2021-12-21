function makeReview() {
    // 핑퐁핑퐁_4번 code 변수 넣어서 변수값 넣어주기
    let code = $('#code').val()
    let author = $('#author').val()
    let review = $('#review').val()
    console.log(name)
    $.ajax({
        type: "POST",
        url: "/review",
        //code 변수 값 넣어주기 code_give : code 그리고 서버로 다시 넘겨주
        data: {code_give: code, author_give: author, review_give: review},
        success: function (response) {
            alert(response["msg"]);
            window.location.reload();
        }
    })
}

$(document).ready(function () {
    showReview();
});
function showReview() {
    //받은 보여주기 code 값 {code_give: code} 새로고침 결과
    let code = $('#code').val()
    $.ajax({
        type: "GET",
        url: "/review/read",
        data: {code_give: code},
        success: function (response) {
            let reviews = response['all_reviews']
            console.log(code)
            for (let i = 0; i < reviews.length; i++) {
                let author = reviews[i]['author']
                let review = reviews[i]['review']
                let num = reviews[i]['num']

                let temp_html = `<div class="review-box">
                                            <p class="show-name">${author}</p>
                                            <p class="show-text">${review}</p>
                                            <button class="review-show-del" onclick="delete_Review(${num})">삭제</button>
                                 </div>`
                $('.review-show').append(temp_html)
            }
        }
    })
}

function delete_Review(num) {
    // alert(num);

    let del_ok = confirm('삭제하시겠습니까?');

    if (del_ok === false)
        return;

    $.ajax({
        type: 'POST',
        url: '/review/delete',
        data: {num_give:num},
        success: function (response) {
            alert(response['msg']);
            location.reload();
        }
    })
}









// $(document).ready(function () {
//     showReview();
// });
//
// function makeReview() {
//     let author = $('#author').val()
//     let review = $('#review').val()
//
//     $.ajax({
//         type: "POST",
//         url: "/api/review",
//         data: {author_give:author, review_give:review},
//         success: function (response) {
//             alert(response["msg"]);
//             window.location.reload();
//         }
//     })
// }
//
// function showReview() {
//     $.ajax({
//         type: "GET",
//         url: "/api/review",
//         data: {},
//         success: function (response) {
//             let reviews = response['all_review']
//             console.log(reviews)
//         }
//     })
// }
