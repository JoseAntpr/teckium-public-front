const $ = require('jquery');
const CommentListManager = require('./comment_list_manager');
//const postListManager = require('./post_list_manager');
const likes = require('./likes');

$(document).ready(function(){

    $('.load-comments').on("click", function(){
        let post_id = document.getElementById("loadComments");
        CommentListManager.loadComments(post_id.value);
    });

    $('.favourite-button').on("click", function(){
        likes.clickLike($(this));
    });

    /*$(window).scroll(function () {
        if($(window).scrollTop() + $(window).height() == $(document).height()) {
            postListManager.loadposts();
        }
    });*/

});
