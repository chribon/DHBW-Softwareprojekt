import { Component, OnInit} from '@angular/core';
import { Category } from '../Models/category';
import { ActivatedRoute } from '@angular/router';
import { Subcategory } from '../Models/subcategory';
import * as L from 'leaflet';
import { icon, Marker } from 'leaflet';
import { FeatureCollection } from '../Models/FeatureCollection/featurecollection';
import { Marker_ID } from '../Models/marker_id';
import { OpeningHours } from '../Models/FeatureCollection/Properties/openingHours';
import { APIService } from '../api.service';



@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {
  category: Category;
  categories: Category[] = [];
  subcategories: Subcategory[];
  subcategoriesFromCategory: Subcategory[] = [];
  title: string;
  selectedSubcategories: Subcategory[] = [];
  map: any;
  markers: Marker_ID[] = [];
  description: string;
  price: string;
  openingHours: OpeningHours;


  constructor(private route: ActivatedRoute,
     private apiService: APIService) { }

  ngOnInit() {
    this.initMap();
     this.apiService.getCategoriesFromAPI().subscribe((Categories) => {
      this.categories = Categories;

     this.route.params.subscribe(params => {
        this.title = params['title'];
        this.category = this.categories.find(category => category.title === this.title);
        this.apiService.getSubcategoriesFromAPI().subscribe((subcategories) => {
          this.subcategories = subcategories;
          this.processQueryParameters();
          this.subcategoriesFromCategory = [];
          for (let key in this.subcategories) {
            if (this.subcategories[key].id_category === this.category.id) {
              this.subcategoriesFromCategory.push(this.subcategories[key]);
            }
          }

        });

      });

    });

  }



  initMap() {
    this.map = L.map('mapid').setView([49.352164, 9.145679], 14);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(this.map);

    /* costum marker
        var greenIcon = L.icon({
          iconUrl: 'assets/marker-icon.png',
          shadowUrl: 'assets/marker-shadow.png',
    
          iconSize: [38, 95], // size of the icon
          shadowSize: [50, 64], // size of the shadow
          iconAnchor: [22, 94], // point of the icon which will correspond to marker's location
          shadowAnchor: [4, 62],  // the same for the shadow
          popupAnchor: [-3, -76] // point from which the popup should open relative to the iconAnchor
        });
     */

     // fix marker image output path
    const iconRetinaUrl = 'assets/marker-icon-2x.png';
    const iconUrl = 'assets/marker-icon.png';
    const shadowUrl = 'assets/marker-shadow.png';
    const iconDefault = icon({
      iconRetinaUrl,
      iconUrl,
      shadowUrl,
      iconSize: [25, 41],
      iconAnchor: [12, 41],
      popupAnchor: [1, -34],
      tooltipAnchor: [16, -28],
      shadowSize: [41, 41]
    });
    Marker.prototype.options.icon = iconDefault;

  }

  toggleSubcategory(subcategory: Subcategory) {

    if (this.selectedSubcategories.some(subcategoryFromArray => subcategoryFromArray.title === subcategory.title)) {
      var index = this.selectedSubcategories.indexOf(subcategory);
      if (index > -1) {
        this.selectedSubcategories.splice(index, 1);
      }
    } else {
      this.selectedSubcategories.push(subcategory);
      this.displayPOIsOnMap(subcategory.id);
    }

  }

  disableClick(subcategory: Subcategory) {
    if (this.selectedSubcategories.some(subcategoryFromArray => subcategoryFromArray.title === subcategory.title)) {
      return true;
    } else {
      return false;
    }
  }

  checkEmptySelectedCategories() {
    if (this.selectedSubcategories.length == 0) {
      return true;
    }
    else {
      return false;
    }
  }

  displayPOIsOnMap(subcategoryID: number) {

    this.apiService.getEntriesFromAPI(subcategoryID).subscribe(FeatureCollection => {

      let featureCollection: FeatureCollection = FeatureCollection;
      console.log(FeatureCollection);
      let markerArray = [];
      let _this = this;

      for (let feature of featureCollection.features) {
        if (feature.geometry.type == "Point") {
        
         let marker = L.geoJSON(feature).addTo(this.map).bindPopup(feature.properties.title)
          .openPopup().on('click', function () {
            console.log(feature.properties.openinghours);
            if (feature.properties.openinghours) {
              _this.openingHours = { monday:feature.properties.openinghours.monday, 
                tuesday:feature.properties.openinghours.monday,
                wednesday:feature.properties.openinghours.monday,
                thursday:feature.properties.openinghours.monday,
                friday:feature.properties.openinghours.monday,
                saturday:feature.properties.openinghours.monday,
                sunday:feature.properties.openinghours.monday };


            }
            if (feature.properties.price) {
              if (feature.properties.price.length > 0) {
                _this.price = feature.properties.price.toString();
              }
            }
            if (feature.properties.description) {
              if (feature.properties.description.length > 0) {
                _this.description = feature.properties.description.toString();
              }
            }

          });
           
          markerArray.push(marker);
        }
        else if (feature.geometry.type == "Polygon") {

          let marker = L.geoJSON(feature).addTo(this.map).bindPopup(feature.properties.title)
          .openPopup().on('click', function () {

            if (feature.properties.openinghours) {
              
              _this.openingHours = { monday:feature.properties.openinghours.monday, 
                tuesday:feature.properties.openinghours.monday,
                wednesday:feature.properties.openinghours.monday,
                thursday:feature.properties.openinghours.monday,
                friday:feature.properties.openinghours.monday,
                saturday:feature.properties.openinghours.monday,
                sunday:feature.properties.openinghours.monday };

              
              
            }
            if (feature.properties.price) {
              if (feature.properties.price.length > 0) {
                _this.price = feature.properties.price.toString();
              }
            }

            if (feature.properties.description) {
              if (feature.properties.description.length > 0) {
                _this.description = feature.properties.description.toString();
              }
            }

          });
           
          markerArray.push(marker);
        }
      }


      let marker_id: Marker_ID = { subcategoryID: subcategoryID, markers: markerArray };
      this.markers.push(marker_id);
    });
  }

  removePOIsFromMap(subcategoryID: number) {
    for (let marker_id of this.markers)
      if (marker_id.subcategoryID == subcategoryID) {
        for (let marker of marker_id.markers) {
          this.map.removeLayer(marker);
          this.price = "";
          this.openingHours = null;
        }
      }
  }
  getCategoryTitleBySubcategoryID(subcategoryID: number): string{
    let category = this.categories.find(category =>(category.id == subcategoryID));
    if(category.title){
      return category.title;
    }
    return "";
  }
  processQueryParameters(){
    this.route.queryParams.subscribe(params => {
      let selectedSubcategoryTitle = params['selectedSubcategory'];
      let selectedSubcategory = this.subcategories.find(Subcategory => Subcategory.title == selectedSubcategoryTitle);
      if(selectedSubcategory){
        this.toggleSubcategory(selectedSubcategory);
      }
    });
  }

}
