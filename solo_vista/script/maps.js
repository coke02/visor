
var map;
 function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
  center: {lat: -33.444371, lng: -70.682343},
      zoom: 13,
    });
    var marker = new google.maps.Marker({
      position: {lat: -33.444371, lng: -70.682343},
      map: map,
    title: 'Quinta Normal'
    });
}
