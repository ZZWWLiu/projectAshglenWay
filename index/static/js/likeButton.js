var $button = $("#nowPlaying button");
var clicked
$button.click(function(event){
	var movie = $(this).val();
	clicked = $(this)
	$.ajax({
		url:"/movies",
		data: {"movie": movie}
	}).done(function () {
		console.log("liked movie: "+ movie);
		$span = clicked.children();
		if($span.text() === "Like") {
			$span.attr("class", "glyphicon glyphicon-star");
			$span.text("Unlike");
		} else {
			$span.attr("class", "glyphicon glyphicon-star-empty");
			$span.text("Like");
		}
	});
});