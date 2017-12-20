function display (locations) {
  var location = locations;
  var map = new google.maps.Map(document.getElementById('mapdiv'), {
    zoom: 4,
    center: location
  });
  var marker = new google.maps.Marker({
    position: location,
    map: map
  });
}

function init () {
  var address = 'London, UK';
  getGeoCode(address);
}

function getGeoCode(address) {
  var geocoder = new google.maps.Geocoder();
  if (geocoder) {
    geocoder.geocode({ 'address': address }, function (results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        console.log(results[0].geometry.location);
        display(results[0].geometry.location);
        return (results);
      }
      else {
        console.log("Geocoding failed: " + status);
      }
    });
  }
  return geocode
}
