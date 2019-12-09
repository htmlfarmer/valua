
function XY(Sender,e){
  var x = e.x - Sender.offsetLeft;
  var y = e.y - Sender.offsetTop;
  document.getElementById('coord').innerHTML = "x = " + x + " y = " + y;
}


function SelectMap(Sender,Event){
  var map = document.getElementById('MapSelection');
  var value = map.options[map.selectedIndex].value;
  var text = map.options[map.selectedIndex].text;
  var image = document.getElementById('MapImage');

  switch(value) {
    case "WorldMap":
    image.src="world.jpg";
    break;
    case "PopulationMap":
    image.src="population.png";
    break;
    case "TopologicalMap":
    image.src="topological.png";
    break;
    case "VegetationMap":
    image.src="vegetation.png";
    break;
    default:
    image.src="world.jpg";
    break;
  }
  return
}

function Size(id){
  var img = document.getElementById(id);
  //or however you get a handle to the IMG
  var width = img.clientWidth;
  var height = img.clientHeight;
}
