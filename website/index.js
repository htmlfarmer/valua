
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

var Conv=({
	r_major:6378137.0,//Equatorial Radius, WGS84
	r_minor:6356752.314245179,//defined as constant
	f:298.257223563,//1/f=(a-b)/a , a=r_major, b=r_minor
	deg2rad:function(d)
	{
		var r=d*(Math.PI/180.0);
		return r;
	},
	rad2deg:function(r)
	{
		var d=r/(Math.PI/180.0);
		return d;
	},
	ll2m:function(lon,lat) //lat lon to mercator
	{
		//lat, lon in rad
		var x=this.r_major * this.deg2rad(lon);

		if (lat > 89.5) lat = 89.5;
		if (lat < -89.5) lat = -89.5;


		var temp = this.r_minor / this.r_major;
		var es = 1.0 - (temp * temp);
		var eccent = Math.sqrt(es);

		var phi = this.deg2rad(lat);

		var sinphi = Math.sin(phi);

		var con = eccent * sinphi;
		var com = .5 * eccent;
		var con2 = Math.pow((1.0-con)/(1.0+con), com);
		var ts = Math.tan(.5 * (Math.PI*0.5 - phi))/con2;
		var y = 0 - this.r_major * Math.log(ts);
		var ret={'x':x,'y':y};
		return ret;
	},
	m2ll:function(x,y) //mercator to lat lon
	{
		var lon=this.rad2deg((x/this.r_major));

		var temp = this.r_minor / this.r_major;
		var e = Math.sqrt(1.0 - (temp * temp));
		var lat=this.rad2deg(this.pj_phi2( Math.exp( 0-(y/this.r_major)), e));

		var ret={'lon':lon,'lat':lat};
		return ret;
	},
	pj_phi2:function(ts, e)
	{
		var N_ITER=15;
		var HALFPI=Math.PI/2;


		var TOL=0.0000000001;
		var eccnth, Phi, con, dphi;
		var i;
		var eccnth = .5 * e;
		Phi = HALFPI - 2. * Math.atan (ts);
		i = N_ITER;
		do
		{
			con = e * Math.sin (Phi);
			dphi = HALFPI - 2. * Math.atan (ts * Math.pow((1. - con) / (1. + con), eccnth)) - Phi;
			Phi += dphi;

		}
		while ( Math.abs(dphi)>TOL && --i);
		return Phi;
	}
});

//usage
// var mercator=Conv.ll2m(47.6035525, 9.770602);//output mercator.x, mercator.y
// var latlon=Conv.m2ll(5299424.36041, 1085840.05328);//output latlon.lat, latlon.lon
