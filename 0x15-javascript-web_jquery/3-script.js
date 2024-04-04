// Uses the jQuery API to change the color to red class to the header tag
// red when the div#red_header tag is clicked

$('div#red_header').click(function () {
    $('header').addClass('red');
  });
