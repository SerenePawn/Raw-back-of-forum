$(document).ready(function () {
    $(".btn").click(testAjax)
});
console.log('script loaded');

function testAjax() {
    $('.result').html('Please, stand by... *fallout theme*')
    $.ajax({
        type: 'GET',
        data: {'de_wei': $('.field').val()},
        dataType: 'text',
        success: function (result) {
            $('.result').html(result)
        }}
    );
    console.log('AJAX request: success');
}