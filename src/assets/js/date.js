<<<<<<< HEAD
const moment = require("moment");
moment.locale('es');
const $ = require("jquery");

module.exports = {
  calcTime: function() {
    initialDate = $(".publication-date");

    initialDate.each(function() {
      let date = moment($(this).text());

      if (moment().diff(moment($(this).text()), "days") > 1) {
        date = date.calendar();
      } else {
        date = date.fromNow();
      }
      $(this).replaceWith("<time class='publication-date'>" + date + "</time>");
    });
  }
};
=======
var moment = require('moment')
>>>>>>> 7765296a89aa97a4d4a6ea73de64119c4d74976f
