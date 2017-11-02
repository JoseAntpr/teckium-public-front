const $ = require("jquery");
const API_URL = "http://ec2-52-87-175-61.compute-1.amazonaws.com/api/1.0/posts/";
//const API_URL = "http://127.0.0.1:8001/api/1.0/posts/";

module.exports = {
  partial_update: function(post_id, likes, successCallBack, errorCallBack) {
    $.ajax({
      url: API_URL + post_id + "/",
      type: "PATCH",
      contentType: 'application/json',
      data: JSON.stringify(likes),
      beforeSend: function (xhr) {
        /* Authorization header */
        xhr.setRequestHeader("Authorization", "JWT " + token);
      },
      success: function(data) {
        successCallBack(data);
      },
      error: function(error) {
        errorCallback(error);
        console.error("Error al guardar el like", error);
      }
    });
  }
};
