function addRight() {
    var ul = document.getElementById("sqnce-list");
    var val = "Right >";
    var li = document.createElement("li");
    li.setAttribute('id', "right");
    li.appendChild(document.createTextNode(val));
    ul.appendChild(li);
}

function addLeft() {
    var ul = document.getElementById("sqnce-list");
    var val = "Left <";
    var li = document.createElement("li");
    li.setAttribute('id', "left");
    li.appendChild(document.createTextNode(val));
    ul.appendChild(li);
}

function addForward() {
    var ul = document.getElementById("sqnce-list");
    var val = "Forward ^";
    var li = document.createElement("li");
    li.setAttribute('id', "forward");
    li.appendChild(document.createTextNode(val));
    ul.appendChild(li);
}

function addBack() {
    var ul = document.getElementById("sqnce-list");
    var val = "Back ˅";
    var li = document.createElement("li");
    li.setAttribute('id', "back");
    li.appendChild(document.createTextNode(val));
    ul.appendChild(li);
}

// function removeItem() {
//     var ul = document.getElementById("sqnce-list");
//     // var item = document.getElementById("id");
//     ul.removeChild(item);
// }