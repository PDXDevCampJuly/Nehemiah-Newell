/**
* Created by Nehemiah on 8/26/2015.
*/

var jumbotron = document.getElementById("jumbotron");
var listOfImages = [];
var currentImage = 3;

(function () {
    var i;
    for(i = 1; i < 10;i++)
    {
        var num = i.toString();
        listOfImages.push("'../static/images/pdxcg_0" + num + ".jpg'");
    }
    for(; i <= 60;i++)
    {
        if(i === 36 || i === 42){i++;} //These two photoes are missing - comment out this line if they're found.
        var num = i.toString();
        listOfImages.push("'../static/images/pdxcg_" + num + ".jpg'");
    }
}());

function changeTheImage()
{
    currentImage++;
    jumbotron.style= "background-image: url(" + listOfImages[currentImage] + ")";
    console.log(currentImage)
    setTimeout(changeTheImage, 20000);

}

changeTheImage();
