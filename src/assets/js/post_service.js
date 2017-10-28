const $ = require('jquery');

module.exports = {

    // recuperar todos los posts
    list: function (successCallback, errorCallback) {
        if (url && url != "None"){
            $.ajax({
                url: url,
                type: "get", // recuperar datos en una API REST
                success: function (data) {
                    console.log(url)
                        url = data.next;
                        successCallback(data);
                    
                },
                error: function (error) {
                    errorCallback(error);
                    console.error("postsServiceError", error);
                }
            });
        }
        
    }

}