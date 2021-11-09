function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function removeNode(node) {
        node.parentNode.removeChild(node);
      }
      
function drop(ev) {
      ev.preventDefault();
      var data = ev.dataTransfer.getData("text");
      var isLeft = 'drag3' == data || "drag4" == data;
      var nodeCopy = document.getElementById(data).cloneNode(true);
      nodeCopy.id = "img" + ev.target.id;
      // clean target space if needed
      if (isLeft) {
        if (ev.target.nodeName == 'IMG') {
          ev.target.parentNode.appendChild(nodeCopy);
          removeNode(ev.target);
        }
        else 
          ev.target.appendChild(nodeCopy);
      }
      else {
        if (ev.target.nodeName != 'IMG') {
          removeNode(document.getElementById(data));
          ev.target.appendChild(nodeCopy);
        }
      }
      ev.stopPropagation();
      return false;
    }

function allowDrop(ev) {
  ev.preventDefault();
}


function savemap() { 
  






}