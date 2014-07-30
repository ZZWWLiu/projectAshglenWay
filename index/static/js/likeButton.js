var $button = $("#nowPlaying button");
var clicked
var $collections_badge = $("#collections .badge")
$button.click(function(event){
	var movie = $(this).val();
	clicked = $(this)
	$.ajax({
		url:"/movies",
		data: {"movie": movie}
	}).done(function () {
		// console.log("liked movie: "+ movie);
		$span = clicked.children();
		num = Number($collections_badge.text());
		if($span.text() === "Like") {
			clicked.attr("class", "btn btn-success btn-sm")
			$span.attr("class", "glyphicon glyphicon-star");
			$span.text("Unlike");
			// collection badge increase
			num = num+1;
		} else {
			clicked.attr("class", "btn btn-warning btn-sm")
			$span.attr("class", "glyphicon glyphicon-star-empty");
			$span.text("Like");
			// collection badge decrease
			num = num-1;

		}
		$collections_badge.text(num)
	});
});