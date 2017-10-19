const moment = require("moment");
moment.locale("es");
const $ = require("jquery");

module.exports = {
  calcTime: function() {
    let self = this;
    initialDate = $(".publication-date");

    initialDate.each(function() {
      let date = $(this).text();

      date = self.dateFormat(date);

      $(this).replaceWith("<time class='publication-date'>" + date + "</time>");
    });
  },
  dateFormat: function(date) {
    date = moment(date)
    
    if (moment().diff(date, "days") > 1) {
      date = date.calendar();
    } else {
      date = date.fromNow();
    }
    return date;
  }
};
