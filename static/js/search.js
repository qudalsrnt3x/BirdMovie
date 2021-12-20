function makeReview() {

    let author = $('#author').val()
    let review = $('#review').val()
    console.log(name)
    $.ajax({
        type: "POST",
        url: "/review",
        data: {author_give: author, review_give: review},
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
    $.ajax({
        type: "GET",
        url: "/review/read",
        data: {},
        success: function (response) {
            let reviews = response['all_reviews']
            for (let i = 0; i < reviews.length; i++) {
                let author = reviews[i]['author']
                let review = reviews[i]['review']

                let temp_html = `<div class="review-box">
                                            <p class="show-name">${author}</p>
                                            <p class="show-text">${review}</p>
                                            <button class="review-show-del" onclick="delete_Review()">삭제</button>`
                $('#review-main').append(temp_html)
            }
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
