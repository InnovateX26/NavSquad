for (let name in locations) {
  var marker = L.marker(locations[name]).addTo(map);
}