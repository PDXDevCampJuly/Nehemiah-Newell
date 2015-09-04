/**
* Created by Nehemiah on 8/26/2015.
*/

var inventory = document.getElementById("inventory");
var materials = [];
var xGrab = new XMLHttpRequest();

function removeStock()
{
    var rows = inventory.getElementsByTagName('tr');
    for(var i = 0; i < rows.length; i++)
    {
        var inputs = rows[i].getElementsByTagName('input');
        if (inputs[0].type === 'checkbox')
        {
            if (inputs[0].checked)
            {
                materials[i].pStock = 0;
            }
        }
    }
    populateInventory();
}

function addStock()
{
    var rows = inventory.getElementsByTagName('tr');
    for(var i = 0; i < rows.length; i++)
    {
        var inputs = rows[i].getElementsByTagName('input');
        if (inputs[0].type === 'checkbox')
        {
            if (inputs[0].checked)
            {
                //flip status
                materials[i].pStock = 10;
            }
        }
    }
    populateInventory();
}

function addNewStock()
{

    material = document.getElementById('material').value;
    price = document.getElementById('price').value;

    if(!(material === "") && !(price === "") && !(isNaN(price)))
    {
        materials.push(new Product(material,0,price,false, materials.length));
        // update screen
        populateInventory();
        document.getElementById('material').value = '';
        document.getElementById('price').value = '';
    }
}

function checkAll(checkAllBox)
{
    var inputs = inventory.getElementsByTagName('input');
    for(var i = 0; i < inputs.length; i++)
    {
        if (inputs[i].type === 'checkbox')
        {
            materials[i].pChecked = checkAllBox.checked;
        }
    }
    populateInventory()
}

function Product(productName, productStock, productPrice, isItChecked, productCount)
{
    this.pName = productName;
    this.pStock = productStock;
    this.pPrice = productPrice;
    this.pChecked = isItChecked;
    this.pCount = productCount;


    this.isCheck = function()
    {
        if(this.pChecked)
        {
            return "checked"
        }
    }

    this.inStock = function()
    {
        if(this.pStock > 0)
        {
            return "true"
        }
        else
        {
            return "false"
        }
    };
    this.printRow = function()
    {
        return "<tr><td><input type='checkbox' " + this.isCheck() + " id='checkbox"+ this.pCount +"' onclick='setBoxToChecked(this)' /></td><td>" + this.pName + "</td><td>$"
            + this.pPrice + "</td><td class='" + this.inStock() + "'>" + this.pStock + "</td></tr>";
    };
}

function populateInventory()
{
    var replaceString = "";
    for(var i = 0; i < materials.length; i++)
    {
        replaceString += materials[i].printRow();
    }
    inventory.innerHTML = replaceString;
}

function setBoxToChecked(idString)
{
    var numb = idString.id.match(/\d/g);
    numb = parseInt(numb.join(""));
    materials[numb].pChecked = idString.checked;
}


xGrab.onload = function()
{
	var responce = xGrab.responceXMl;
	var invent = response.getElementsByTagName('item');
	for (var i = 0; i < invent.length; i++)
	{
		materials.push(new Product(invent[i].getAttributeNode("name"),getNodeValue(invent[i],'numInStock'),invent[i].getAttributeNode("price"),false, materials.length));
	}
	
}

xGrab.open('GET','data/data.xml',true);
xGrab.send(null);
populateInventory();