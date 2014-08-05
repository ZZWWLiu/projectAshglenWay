var $del = $(".liked-movie button");
var $collections_badge = $("#collections .badge");
var clicked

$del.click(function(){
	var movie = $(this).val();
	clicked = $(this);
	$.ajax({
		url:"",
		data: {"movie": movie}
	}).done(function () {
		num = Number($collections_badge.text());		
		clicked.parent().parent().parent().fadeOut();
		// collection badge decrease
		$collections_badge.text(num-1);
	});

});