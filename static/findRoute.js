var routeLine;

function findRoute() {
  var start = document.getElementById("start").value;
  var end = document.getElementById("end").value;

  var startCoords = locations[start];
  var endCoords = locations[end];

  if (routeLine) {
    map.removeLayer(routeLine);
  }

  routeLine = L.polyline([startCoords, endCoords], {
    color: "red",
    weight: 4
  }).addTo(map);

  map.fitBounds(routeLine.getBounds());
}