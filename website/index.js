
function XY(Sender,e){
  var x = e.x - Sender.offsetLeft;
  var y = e.y - Sender.offsetTop;
  document.getElementById('coord').innerHTML = "x = " + x + " y = " + y;
  LATLON(x, y);
  Specs(document.getElementById('MapImage'), document.getElementById('mapsizes'))
}

function LATLON(x, y) {
  var img = document.getElementById('MapImage');
  var width = img.clientWidth;
  var height = img.clientHeight;
  var world = {width : width, height : height, meridian : 623, equator : 300};
  // Latitude ranges from 0° at the Equator to 90° + for north
  var latitude = y;
  // Longitude ranges from 0° +180° eastward and  0° to −180° westward
  var longitude = x;
  var latlon = {latitude : latitude, longitude : longitude};
  if (y < world["equator"]) {
    latitude = (world["equator"] - y)*90/height;
  } else {
    latitude = (y - world["equator"])*90/height;
  }
  if (x < world["meridian"]) {
    longitude = (-world["meridian"] + x)*180/width;
  } else {
    longitude = (x - world["meridian"])*180/width;
  }

  document.getElementById('latlon').innerHTML = "latitude = " + latitude + " logitude = " + longitude;
  return
}

function Specs(element, placement) {
  var img = element; //document.getElementById('MapImage');
  var width = img.clientWidth;
  var height = img.clientHeight;
  placement.innerHTML = "width = " + width + " height = " + height;
  return
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
