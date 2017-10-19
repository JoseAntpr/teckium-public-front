const $ = require('jquery');

module.exports = {
    list: function(successCallBack, errorCallBack){
        if (url){
            $.ajax({
                url: url,
                type: "get",
                success: function(data){
                    console.log(url)
                    url = data.next;
                    successCallBack(data);
                },
                error: function(error){
                    console.error("Error al recuperar los comentarios", error);
                }
                
            });
        }    
    },
}