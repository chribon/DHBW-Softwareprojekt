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

	L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1Ijoic3RyYWlnaHRlciIsImEiOiJjazRmc3Q1NXAwcG1sM3RvMmExbGdqbGt2In0.RwSVBnVl6hNJn_avx5DIug', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox/streets-v11'
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
