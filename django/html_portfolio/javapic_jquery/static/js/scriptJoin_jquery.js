/**
* Created by Nehemiah on 8/26/2015.
*/
//  Get the whole form, and set basic check flags to false
var $signUpForm = $('.signup');
var $submitButton = $('#submit');
var $labels = $('label');
var $inputs = $('input');
var nameFlag = false;
var userNameFlag = false;
var emailFlag = false;
var pName;

//start the listeners
$submitButton.on('click',submitWatch);
$signUpForm.on("focusin",overWatchFocus).on("focusout",overWatchBlur).on("input",overWatchInput);


// Add a local css sheet with useful classes.
$("head").append("<style id='dynamicStylesheet'></style>");
$("#dynamicStylesheet").text(
"label {position: relative;}" +
"label[for=name].bad:after{display: inline-block;" +
"position: absolute; box-shadow: 10px 5px 5px black; opacity: 0.75;" +
"left: 13em; width: 10em; height: 2.5em; background: red; color:" +
"white; border-radius: 12px; border 2px solid black; padding: .25em; " +
"content: 'Please enter valid name.';}" +
"label[for=username].bad:after{display: inline-block;" +
"position: absolute; box-shadow: 10px 5px 5px black; opacity: 0.75;" +
"left: 13em; width: 10em; height: 2.5em; background: red; color:" +
"white; border-radius: 12px; border 2px solid black; padding: .25em; " +
"content: 'Please enter valid username.';}" +
"label[for=email].bad:after{display: inline-block;" +
"position: absolute; box-shadow: 10px 5px 5px black; opacity: 0.75;" +
"left: 13em; width: 10em; height: 2.5em; background: red; color:" +
"white; border-radius: 12px; border 2px solid black; padding: .25em; " +
"content: 'Please enter valid email address.';}" +
"label[for=name].good:after{display: inline-block;" +
"position: absolute; box-shadow: 10px 5px 5px black; opacity: 0.75;" +
"left: 13em; width: 10em; height: 2.5em; background: blue; color:" +
"white; border-radius: 12px; border 2px solid black; padding: .25em; " +
"content: 'That Name is valid.';}" +
"label[for=username].good:after{display: inline-block;" +
"position: absolute; box-shadow: 10px 5px 5px black; opacity: 0.75;" +
"left: 13em; width: 10em; height: 2.5em; background: blue; color:" +
"white; border-radius: 12px; border 2px solid black; padding: .25em; " +
"content: 'That Username is Valid.';}" +
"label[for=email].good:after{display: inline-block;" +
"position: absolute; box-shadow: 10px 5px 5px black; opacity: 0.75;" +
"left: 13em; width: 10em; height: 2.5em; background: blue; color:" +
"white; border-radius: 12px; border 2px solid black; padding: .25em; " +
"content: 'That is a valid Email Address.';}"
);

//set up the functions to manage the watches

function overWatchFocus(e)
{
    if(e.target.name !== "" && e.target.name !== "submit") {
        verifyGood(e);
    }
}

function overWatchBlur(e)
{
    if(e.target.name !== "" && e.target.name !== "submit") {
		if (e.target.name === "name")
		{
			$labels.eq(0).attr('class','');
		}
		else if (e.target.name === "username")
		{
			$labels.eq(1).attr('class','');
		}
		else if (e.target.name === "email")
		{
			$labels.eq(2).attr('class','');
		}    
    }
}

function overWatchInput(e)
{
    if(e.target.name !== "" && e.target.name !== "submit") {
        verifyGood(e)
    }
}

function submitWatch(e)
{
	// turn off normal submit
    e.preventDefault()
    e.stopPropagation()
	
	// now add new behavor
    if(nameFlag === false)
    {
        $inputs.eq(0).focus();
    }
    else if(userNameFlag === false)
    {
        $inputs.eq(1).focus();
    }
    else if(emailFlag === false)
    {
        $inputs.eq(2).focus();
    }
    else
    {
        sessionStorage.setItem('name', pName);
		$(location).attr('href','../gallery.html');
    }
}


//Checks if the information in the target fulfills our needs for entry.
function verifyGood(eObject)
{
    // It needs to be created now, even if it might be removed right after,
    // because of edge cases where we might remove it without it being present.
    var patt;
    if (eObject.target.name === "name")
    {
        patt = /^[a-z]+/i;
        if (patt.test(eObject.target.value)) //some check
        {
            //removeIt();
            $labels.eq(0).attr('class','good');
            nameFlag = true;
            pName = eObject.target.value;
        }
        else
        {
			$labels.eq(0).attr('class','bad');
            nameFlag = false;
        }
    }
    else if (eObject.target.name === "username")
    {
        patt = /^[a-z]+/i;
        if (patt.test(eObject.target.value)) //some check
        {
            $labels.eq(1).attr('class','good');
            userNameFlag = true;
        }
        else
        {
            $labels.eq(1).attr('class','bad');
			userNameFlag= false;
        }
    }
    else if (eObject.target.name === "email")
    {
        patt = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i;
        if (patt.test(eObject.target.value)) //some check
        {
            $labels.eq(2).attr('class','good');
            emailFlag = true;
        }
        else
        {
			$labels.eq(2).attr('class','bad');
            emailFlagFlag = false;
        }
    }
}


