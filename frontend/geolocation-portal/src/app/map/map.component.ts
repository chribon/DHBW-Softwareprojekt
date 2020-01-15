import { Component, OnInit } from '@angular/core';
import { Category } from '../Models/category';
import { ActivatedRoute } from '@angular/router';
import { Subcategory } from '../Models/subcategory';
import * as L from 'leaflet';
import { icon, Marker } from 'leaflet';
import { FeatureCollection } from '../Models/FeatureCollection/featurecollection';
import { Marker_ID } from '../Models/marker_id';
import { OpeningHours } from '../Models/FeatureCollection/Properties/openingHours';
import { APIService } from '../api.service';
import { Adress } from '../Models/FeatureCollection/Properties/adress';
import { InfoObject } from '../Models/FeatureCollection/Properties/infoObject';
import { Description } from '../Models/FeatureCollection/Properties/description';
import { Price } from '../Models/FeatureCollection/Properties/price';
import { Property } from '../Models/FeatureCollection/property';



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
  mapInfo: boolean = false;
  polygonStyle = {
    "color": "#812323",
    "weight": 1,
    "opacity": 0.65
  };
  
  properties: InfoObject[] = [];

  //properties
  description: string;
  price: string;
  openingHours: OpeningHours;
  adress: Adress;


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
    //openstreetmap de 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
    L.tileLayer('https://{s}.tile.openstreetmap.se/hydda/full/{z}/{x}/{y}.png', {
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
    const iconRetinaUrl = 'assets/images/marker-icon-2x-red.png';
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
              _this.properties = [];
              console.log(feature.properties.openinghours);
              if (feature.properties.openinghours) {

                let openingHours: OpeningHours = new OpeningHours(
                  feature.properties.openinghours.monday, 
                  feature.properties.openinghours.tuesday, 
                  feature.properties.openinghours.wednesday,
                   feature.properties.openinghours.thursday, 
                   feature.properties.openinghours.friday,
                    feature.properties.openinghours.saturday,
                     feature.properties.openinghours.sunday);

                _this.properties.push(openingHours);
                console.log(_this.properties);
                _this.mapInfo = true;
                _this.overridePropertyClassVariable();

              }
              if (feature.properties.adress) {
                let adress: Adress = new Adress( 
                  feature.properties.adress.street, 
                  feature.properties.adress.housenumber,
                  feature.properties.adress.zipcode,
                  feature.properties.adress.city );

                _this.properties.push(adress);
                _this.mapInfo = true;
                _this.overridePropertyClassVariable();
              }
              if (feature.properties.price) {
                if (feature.properties.price.length > 0) {
                  let price = feature.properties.price.toString();

                  _this.properties.push(new Price(price, "price"));
                  _this.mapInfo = true;
                  _this.overridePropertyClassVariable();
                }
              }
              if (feature.properties.description) {
                if (feature.properties.description.length > 0) {
                  let description = feature.properties.description.toString();

                  _this.properties.push(new Description(description, "description"));
                  _this.mapInfo = true;
                  _this.overridePropertyClassVariable();
                }
              }

            });

          markerArray.push(marker);
        }
        else if (feature.geometry.type == "Polygon") {

          let marker = L.geoJSON(feature, {
            style: this.polygonStyle
          }).addTo(this.map).bindPopup(feature.properties.title)
            .openPopup().on('click', function () {
              _this.properties = [];
              if (feature.properties.openinghours) {

                let openingHours: OpeningHours = new OpeningHours(
                  feature.properties.openinghours.monday,
                   feature.properties.openinghours.tuesday, 
                   feature.properties.openinghours.wednesday, 
                   feature.properties.openinghours.thursday, 
                   feature.properties.openinghours.friday, 
                   feature.properties.openinghours.saturday, 
                   feature.properties.openinghours.sunday);
                _this.properties.push(openingHours);
                _this.mapInfo = true;
                _this.overridePropertyClassVariable();

              }
              if (feature.properties.adress) {

                let adress: Adress = new Adress( 
                  feature.properties.adress.street, 
                  feature.properties.adress.housenumber,
                  feature.properties.adress.zipcode,
                  feature.properties.adress.city );
                _this.properties.push(adress);
                _this.mapInfo = true;
                _this.overridePropertyClassVariable();
              }
              if (feature.properties.price) {
                if (feature.properties.price.length > 0) {
                  let price = feature.properties.price.toString();

                  _this.properties.push(new Price(price, "price"));

                  console.log(_this.properties);
                  _this.mapInfo = true;
                  _this.overridePropertyClassVariable();
                }
              }

              if (feature.properties.description) {
                if (feature.properties.description.length > 0) {
                  let description = feature.properties.description.toString();

                  _this.properties.push(new Description(description, "description"));
                  _this.mapInfo = true;
                  _this.overridePropertyClassVariable();
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
          this.description = "";
        }
      }
  }
  getCategoryTitleBySubcategoryID(subcategoryID: number): string {
    let category = this.categories.find(category => (category.id == subcategoryID));
    if (category.title) {
      return category.title;
    }
    return "";
  }
  processQueryParameters() {
    this.route.queryParams.subscribe(params => {
      let selectedSubcategoryTitle = params['selectedSubcategory'];
      let selectedSubcategory = this.subcategories.find(Subcategory => Subcategory.title == selectedSubcategoryTitle);
      if (selectedSubcategory) {
        this.toggleSubcategory(selectedSubcategory);
      }
    });
  }

  overridePropertyClassVariable() {

    this.price = "";
    this.adress = null;
    this.openingHours = null;
    this.description = "";

    this.properties.forEach(property => {
      if (property instanceof Adress) {
        this.adress = property;
      }
      if (property instanceof OpeningHours) {
        console.log("got here");
        this.openingHours = property;
      }
      if (property instanceof Description) {
        this.description = property.description;
      }
      if (property instanceof Price) {
        this.price = property.price;
      }


    });
  }


}
