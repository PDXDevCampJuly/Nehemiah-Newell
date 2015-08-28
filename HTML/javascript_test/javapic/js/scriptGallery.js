/**
* Created by Nehemiah on 8/27/2015.
*/
console.log("The name is: " + sessionStorage.getItem("name"));
//  This script will handle adding images, focusing on them, and unfocusing on
//  them.

//  Declare the universal variables used by the script.
var gallery = document.getElementById("gallery");
var imageToDisplay = document.getElementById("image_show");
var pageHeading = document.getElementsByClassName("tagline");
pageHeading = pageHeading[0];
var displayFlag = false;

//  Populate the page with images.
(function () {
    var i;
    var insertionString = "<ul>";
    for(i = 1; i < 10;i++)
    {
        var num = i.toString();
        insertionString += "<li><img src='images/pdxcg_0" + num + ".jpg' /></li>";
    }
    for(; i <= 60;i++)
    {
        if(i === 36 || i === 42){i++;} //These two photoes are missing - comment out this line if they're found.
        var num = i.toString();
        insertionString += "<li><img src='images/pdxcg_" + num + ".jpg' /></li>";
    }

    insertionString += "</ul>";
    gallery.innerHTML = insertionString;
}());

//print the name

(function () {
    var theName = sessionStorage.getItem("name");

    if (theName !== "" && theName !== undefined)
    {
        pageHeading.innerHTML += theName;
    }
    else
    {
        pageHeading.innerHTML += "Waldo";
    }

}());


//  Add the general purpose event listener that will let you focus in om images.
gallery.addEventListener("click",overWatch, false);
//  Add a listener for when images have been focused on.
imageToDisplay.addEventListener("click",blurOut, false);

function overWatch(e)
{
    // if the item clicked on is an img
    if (e.target.tagName === "IMG")
    {
        //focus on it.
        focusOn(e.target);
    }
}
function blurOut(e)
{
    //If an image is in focus and a click happens off of it...
    if (displayFlag === true && e.target.tagName !== "IMG") {
        //unfocus from it.
        imageToDisplay.className = "display_none";
        displayFlag = true;
    }
}
function focusOn(focusImage)
{
    //Focus on the image selected.
    imageToDisplay.className = "display_img";
    imageToDisplay.firstElementChild.src= focusImage.src;
    displayFlag = true;
}
