// gives and displays random whole number between 1 and 188 (inclusive)
//function randomEp() {
//	var randomNum = Math.floor(Math.random() * (188 - 1 + 1)) + 1;
//	document.getElementById("epDisplay").innerHTML = x[randomNum];//Math.floor(Math.random() * (188 - 1 + 1)) + 1;
//}
$( document ).ready(function() { // loads jquery
	$( "#epbtn" ).click(function() { // when class #btn is clicked
		$.get( "{{ episodes }}")
	})
}