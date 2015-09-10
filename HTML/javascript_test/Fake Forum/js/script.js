/**
* Created by Nehemiah on 9/08/2015.
*/

// declare variables
var postTitle = document.getElementById('postTitle');
var $postBody = document.getElementById('postBody');

//tie a listener to the button
$('#submit').on('click', function()
{
 	//send the post to the server
	$.ajax({
    type: "POST",
    url: "https://docs.google.com/forms/d/1blH7mM6udvlyJ0SrPmbXoNPZg8XCqDQaxHTPrK0HQbA/formResponse",
    data: {"entry_434124687":postTitle.value,"entry_1823097801":postBody.value},
    dataType: "xml",
	// These don't do much, but if I take them out the code stops working.
    success: console.log("Sent"),
    failure: console.log("failed")
}); 
}
);

//get the posts from the server
callUpPage()
//refresh the page
setInterval(callUpPage, 3000);

//talk to the google server to get the page
function callUpPage()
{
	$.ajax({
	   url: "https://spreadsheets.google.com/feeds/list/1ntmcFZk4R0Owmez5eKc0bcu_PftAKwWyXDWTqmypPgI/default/public/values?alt=json-in-script",
	   data:{format: 'json'},
	   dataType: 'jsonp', 
	   type: 'GET',
	   success: function(callBack){buildPage(callBack.feed.entry)}})	
}

// use the posts to build a page.
function buildPage(contents)
{
	var pageContents = "";
	for(var i = 0; i < contents.length; i++)
	{
		//build a page.
		pageContents += "<div class= 'post'><h2>" + contents[i].gsx$posttitle.$t + " made on " + contents[i].gsx$timestamp.$t + "</h2><p>" + contents[i].gsx$postbody.$t + "</p></div>";
	}
	//now load it.
	$(".mainContent").html(pageContents);
}
