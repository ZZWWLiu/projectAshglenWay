//Problem: User when clicking on image goes to a dead end
//Solution: Create a Lightbox

var $overlay = $('<div id="overlay"></div>'); 
var $image = $("<img>");
var $caption = $("<p></p>");

//An image
$overlay.append($image);
//A caption
$overlay.append($caption);
//Add overlay
$("body").append($overlay);

//1. Capture the click event on a link to an image
$("#nowPlaying a").click(function( event ){
	event.preventDefault();
  var href = $(this).attr("href");
  //update overlay with the image linked in the link
  $image.attr("src", href);
  //Get child/s alt attribute and set caption
  var captionText = $(this).children("img").attr("alt");
  $caption.text(captionText);
  //Show the overlay
  $overlay.show();	
});
 
//when overlay is clicked 
$overlay.click(function () {
	$overlay.hide();
});

  //Hide the overlay