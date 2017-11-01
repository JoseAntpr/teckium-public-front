const $ = require('jquery');

module.exports = {
    list: function(successCallBack, errorCallBack){
        if (urlcomments){
            $.ajax({
                url: urlcomments,
                type: "get",
                success: function(data){
                    urlcomments = data.next;
                    successCallBack(data);
                },
                error: function(error){
                    console.error("Error al recuperar los comentarios", error);
                }
                
            });
        }    
    },
}