const $ = require('jquery');
const CommentListManager = require('./comment_list_manager');

$(document).ready(function(){

    $('.load-comments').on("click", function(){
        let post_id = document.getElementById("loadComments");
        CommentListManager.loadComments(post_id.value);
    });

});