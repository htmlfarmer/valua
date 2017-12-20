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

function initMap () {
  var geocoder = new google.maps.Geocoder();
  var address = 'London, UK';
  if (geocoder) {
    geocoder.geocode({ 'address': address }, function (results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        console.log(results[0].geometry.location);
        display(results[0].geometry.location);
      }
      else {
        console.log("Geocoding failed: " + status);
      }
    });
  }
}
