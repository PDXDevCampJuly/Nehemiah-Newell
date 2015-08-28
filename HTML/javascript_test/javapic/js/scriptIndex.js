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
        listOfImages.push("'images/pdxcg_0" + num + ".jpg'");
    }
    for(; i <= 60;i++)
    {
        if(i === 36 || i === 42){i++;} //These two photoes are missing - comment out this line if they're found.
        var num = i.toString();
        listOfImages.push("'images/pdxcg_" + num + ".jpg'");
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