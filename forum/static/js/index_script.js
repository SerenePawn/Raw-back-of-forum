$(document).ready(function () {
    console.log('Document loaded');

    $('.topic').click(function () {
        var topic_id = $(this).attr('id');
         $.ajax('topics/' + topic_id, {
             type: 'GET',
             data: {'topic_id': topic_id},
             dataType: 'text',
             success: function (result) {
                 $('body').html(result)
             }
        });
         window.history.replaceState({}, '', '/topics/' + topic_id);

    })
});
