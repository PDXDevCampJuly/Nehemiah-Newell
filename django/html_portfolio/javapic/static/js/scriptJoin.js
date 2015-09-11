/**
* Created by Nehemiah on 8/26/2015.
*/
//  Get the whole form, and set basic check flags to false
var signUpForm = document.getElementsByClassName("signup");
var submitButton = document.getElementById("submit");
var nameFlag = false;
var userNameFlag = false;
var emailFlag = false;
var pName;

signUpForm.attribute = "Action = 'gallery.html'";

// Add a local css sheet that can be dynamically changed.
var sheet = (function() {
	// Create the <style> tag
	var style = document.createElement("style");

	// Add a media (and/or media query) here if you'd like!
	// style.setAttribute("media", "screen")
	// style.setAttribute("media", "only screen and (max-width : 1024px)")

	// WebKit hack :(
	style.appendChild(document.createTextNode(""));

	// Add the <style> element to the page
	document.head.appendChild(style);

	return style.sheet;
})();



// Set labels to relative for placing popup bubbles
sheet.insertRule("label {position: relative;", 0);

// creates a pop up bubble attached to a named relative element with color and
// text chosen at the moment of creation.
function createValidBox(aim, color, text)
{
    sheet.insertRule("label[for="+ aim + "]:after{display: inline-block;" +
        "position: absolute; box-shadow: 10px 5px 5px black; opacity: 0.75;" +
        "left: 13em; width: 10em; height: 2.5em; background: "+ color +"; color:" +
        "white; border-radius: 12px; border 2px solid black; padding: .25em; " +
        "content: '"+ text +"';",1);
}

// removes a bubble created with the above function. ALWAYS remove a bubble
// before creating the next, or it will become impossible to remove/update it.
function removeIt()
{
    sheet.deleteRule(1)
}

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
        removeIt();
    }
}

function overWatchInput(e)
{
    if(e.target.name !== "" && e.target.name !== "submit") {
        removeIt();
        verifyGood(e)
    }
}

function submitWatch(e)
{
    e.preventDefault()
    e.stopPropagation()
    var refocus;
// turn off normal submit
    if(nameFlag === false)
    {
        refocus = document.getElementsByName('name');
        refocus[0].focus();
    }
    else if(userNameFlag === false)
    {
        refocus = document.getElementsByName('username');
        refocus[0].focus();
    }
    else if(emailFlag === false)
    {
        refocus = document.getElementsByName('email');
        refocus[0].focus();
    }
    else
    {
        sessionStorage.setItem('name', pName);
        document.location.href = "../gallery.html"
    }
}

// print the red box of failure
function callBox(data)
{
    createValidBox(data.target.name,"red","Please fill in valid information.");
}


//Checks if the information in the target fulfills our needs for entry.
function verifyGood(eObject)
{
    // It needs to be created now, even if it might be removed right after,
    // because of edge cases where we might remove it without it being present.
    callBox(eObject);
    var patt;
    if (eObject.target.name === "name")
    {
        patt = /^[a-z]+/i;
        if (patt.test(eObject.target.value)) //some check
        {
            removeIt();
            createValidBox(eObject.target.name,"Blue","Good!");
            nameFlag = true;
            pName = eObject.target.value;
        }
        else
        {
            nameFlag = false;
        }
    }
    else if (eObject.target.name === "username")
    {
        patt = /^[a-z]+/i;
        if (patt.test(eObject.target.value)) //some check
        {
            removeIt();
            createValidBox(eObject.target.name,"blue","Good!");
            userNameFlag = true;
        }
        else
        {
            userNameFlag= false;
        }
    }
    else if (eObject.target.name === "email")
    {
        patt = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i;
        if (patt.test(eObject.target.value)) //some check
        {
            removeIt();
            createValidBox(eObject.target.name,"blue","Good!");
            emailFlag = true;
        }
        else
        {
            emailFlagFlag = false;
        }
    }
}


//start the listeners

signUpForm[0].addEventListener("focus",overWatchFocus, true);
signUpForm[0].addEventListener("blur",overWatchBlur, true);
signUpForm[0].addEventListener("input",overWatchInput, true);
submitButton.addEventListener("click",submitWatch,true);

//
//var str = "Abc: Lorem ipsum sit amet";
//str = str.split(":").pop();
//alert(str);
//
//populateInventory()
//
//function removeStock()
//{
//    var rows = inventory.getElementsByTagName('tr');
//    for(var i = 0; i < rows.length; i++)
//    {
//        var inputs = rows[i].getElementsByTagName('input');
//        if (inputs[0].type === 'checkbox')
//        {
//            if (inputs[0].checked)
//            {
//                materials[i].pStock = 0;
//            }
//        }
//    }
//    populateInventory();
//}
//
//function addStock()
//{
//    var rows = inventory.getElementsByTagName('tr');
//    for(var i = 0; i < rows.length; i++)
//    {
//        var inputs = rows[i].getElementsByTagName('input');
//        if (inputs[0].type === 'checkbox')
//        {
//            if (inputs[0].checked)
//            {
//                //flip status
//                materials[i].pStock = 10;
//            }
//        }
//    }
//    populateInventory();
//}
//
//function addNewStock()
//{
//
//    material = document.getElementById('material').value;
//    price = document.getElementById('price').value;
//
//    if(!(material === "") && !(price === "") && !(isNaN(price)))
//    {
//        materials.push(new Product(material,0,price,false, materials.length));
//        // update screen
//        populateInventory();
//        document.getElementById('material').value = '';
//        document.getElementById('price').value = '';
//    }
//}
//
//function checkAll(checkAllBox)
//{
//    var inputs = inventory.getElementsByTagName('input');
//    for(var i = 0; i < inputs.length; i++)
//    {
//        if (inputs[i].type === 'checkbox')
//        {
//            materials[i].pChecked = checkAllBox.checked;
//        }
//    }
//    populateInventory()
//}
//
//function Product(productName, productStock, productPrice, isItChecked, productCount)
//{
//    this.pName = productName;
//    this.pStock = productStock;
//    this.pPrice = productPrice;
//    this.pChecked = isItChecked;
//    this.pCount = productCount;
//
//
//    this.isCheck = function()
//    {
//        if(this.pChecked)
//        {
//            return "checked"
//        }
//    }
//
//    this.inStock = function()
//    {
//        if(this.pStock > 0)
//        {
//            return "true"
//        }
//        else
//        {
//            return "false"
//        }
//    };
//    this.printRow = function()
//    {
//        return "<tr><td><input type='checkbox' " + this.isCheck() + " id='checkbox"+ this.pCount +"' onclick='setBoxToChecked(this)' /></td><td>" + this.pName + "</td><td>$"
//            + this.pPrice + "</td><td class='" + this.inStock() + "'>" + this.pStock + "</td></tr>";
//    };
//}
//
//function populateInventory()
//{
//    var replaceString = "";
//    for(var i = 0; i < materials.length; i++)
//    {
//        replaceString += materials[i].printRow();
//    }
//    inventory.innerHTML = replaceString;
//}
//
//populateInventoryDOM()
//{
//    for(var i = 0; i < materials.length; i++)
//    {
//        var newProdRow = document.createElement("tr");
//        var checkboxCell = document.createElement('td');
//        var checkbox = document.createElement('input');
//        checkbox.type = "checkbox";
//        checkbox.checked = materials[i].pChecked;
//        checkboxCell.appendChild(checkbox);
//        newProdRow.appendChild(checkboxCell);
//
//        //name column
//        var nameCol = document.createElement('td');
//        var nameText = document.createTextNode(materials[i].pName)
//        nameCol.appendChild(nameText)
//        newProdRow.appendChild((nameCol))
//
//        //price column
//        var priceCol = document.createElement('td');
//        var priceText = document.createTextNode('$' + materials[i].pPrice)
//        nameCol.appendChild(priceText)
//        newProdRow.appendChild((priceCol))
//
//        //Stock column
//        var stockCol = document.createElement('td');
//        stockCol.className = materials[i].inStock()
//        var stockText = document.createTextNode(materials[i].pStock)
//        nameCol.appendChild(stockText)
//        newProdRow.appendChild((stockCol))
//
//    }
//}
//
//
//function setBoxToChecked(idString)
//{
//    var numb = idString.id.match(/\d/g);
//    numb = parseInt(numb.join(""));
//    materials[numb].pChecked = idString.checked;
//}