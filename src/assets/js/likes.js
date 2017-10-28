const $ = require('jquery');
const likeService = require('./likes_service');

module.exports = {
    clickLike: function(post_id){
        let self = this;
        let likes = JSON.parse(post_id.val());
        let post = $(post_id).attr("id");
        if($(post_id).attr("data-action") === "upvote"){
            likes.push(parseInt(user));
            console.log(likes);
            likeService.partial_update(post, {likes:likes},
            function(data){
                console.log("Likes guardados", data)
            }, function(error){
                console.log("Se ha producido un error");
            });
            $(post_id).attr("data-action","unvote");
            $(post_id).children().removeClass();
            $(post_id).children().addClass("fa fa-heart");
            $(post_id).children().text(" " + (parseInt($(post_id).children().text()) + 1 ));
            

        }else{
            let newLikes = removeElementFromArray(likes, parseInt(user));
            console.log(newLikes);
            likeService.partial_update(post, {likes: newLikes},
                function(data){
                    console.log("Like borrados")
                }, function(error){
                    console.log("Se ha producido un error");
            });
            $(post_id).attr("data-action","upvote");
            $(post_id).children().removeClass();
            $(post_id).children().addClass("fa fa-heart-o");
            $(post_id).children().text(" " + (parseInt($(post_id).children().text()) - 1 ));

        }
    }
}

function removeElementFromArray (array, element){
    let i = array.indexOf(element);
    if(i != -1) {
        array.splice(i, 1);
    }
    return array;
}