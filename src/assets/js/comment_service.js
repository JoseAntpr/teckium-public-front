const $ = require('jquery');
const API_URL = "http://127.0.0.1:8001/api/1.0/comments/"

module.exports = {
    list: function(post_pk, successCallBack, errorCallBack){
        $.ajax({
            url: API_URL + "?page=2&post=" + post_pk,
            type: "get",
            success: function(data){
                successCallBack(data);
            },
            error: function(error){
                console.error("Error al recuperar los comentarios", error);
            }
            
        });
    },
}