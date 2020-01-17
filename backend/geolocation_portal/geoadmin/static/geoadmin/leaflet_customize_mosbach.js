/* Customize leaflet in the admin panel
 *
 * Please note, that we have to write the javascript leaflet agnostic,
 * that is, it has to work if there are 0,1,2, ..., n leaflet-maps in the admin panel!
 * This file is loaded on all admin pages!
*/
window.addEventListener("map:init", function (event) {
//    window.alert("map is loaded");
	var map = event.detail.map;
	console.log(map);

	L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
		maxZoom: 19,
		attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
	}).addTo(map);

	map.setZoom(13);
	var mosbach = L.latLng(49.352554, 9.145346);
	map.panTo(mosbach);

	L.control.fullscreen({
		position: 'topleft',
		title: 'Im Vollbild anzeigen',
		titleCancel: 'Vollbild verlassen'
	}).addTo(map);
});
