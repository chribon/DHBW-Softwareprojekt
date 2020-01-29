import { Component, OnInit } from '@angular/core';
import { Category } from '../Models/category';
import { ActivatedRoute } from '@angular/router';
import { Subcategory } from '../Models/subcategory';
import * as L from 'leaflet';
import 'leaflet.fullscreen';
import { icon, Marker } from 'leaflet';
import { FeatureCollection } from '../Models/FeatureCollection/featurecollection';
import { Marker_ID } from '../Models/marker_id';
import { OpeningHours } from '../Models/FeatureCollection/Properties/openingHours';
import { APIService } from '../api.service';
import { Address } from '../Models/FeatureCollection/Properties/address';
import { InfoObject } from '../Models/FeatureCollection/Properties/infoObject';
import { Description } from '../Models/FeatureCollection/Properties/description';
import { Price } from '../Models/FeatureCollection/Properties/price';
import { Feature } from '../Models/FeatureCollection/feature';
import * as $ from 'jquery';
import { Subcategory_ArrayIndex } from '../Models/subcategory_arrayindex';
import { Areanumber } from '../Models/FeatureCollection/Properties/areanumber';
import { Buildingyear } from '../Models/FeatureCollection/Properties/buildingyear';
import { Denomination } from '../Models/FeatureCollection/Properties/denomination';
import { Difficulty } from '../Models/FeatureCollection/Properties/difficulty';
import { Length } from '../Models/FeatureCollection/Properties/length';
import { No_Free_Buildingplaces } from '../Models/FeatureCollection/Properties/no_free_buildingplaces';
import { No_Places } from '../Models/FeatureCollection/Properties/no_places';
import { School_Type } from '../Models/FeatureCollection/Properties/school_type';
import { Using_Type } from '../Models/FeatureCollection/Properties/using_type';
import { No_Buildingplaces } from '../Models/FeatureCollection/Properties/no_buildingplaces';



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
  selectedSubcategories: Subcategory[] = [];
  title: string = "";
  map: any;
  markers: Marker_ID[] = [];
  subcategoryArrayIndex: Subcategory_ArrayIndex[] = [];
  mapInfo: boolean = false;
  polygonStyle = {
    "color": "#812323",
    "weight": 1,
    "opacity": 0.65
  };

  properties: InfoObject[] = [];

  //properties
  description: Description;
  price: Price;
  openingHours: OpeningHours;
  address: Address;
  areanumber: Areanumber;
  buildingyear: Buildingyear;
  denomination: Denomination;
  difficulty: Difficulty;
  length: Length;
  no_buildingplaces: No_Buildingplaces;
  no_free_buildingplaces: No_Free_Buildingplaces;
  no_places: No_Places;
  school_type: School_Type;
  using_type: Using_Type;



  constructor(private route: ActivatedRoute,
    private apiService: APIService) { }

  ngOnInit() {

    this.initMap();
    this.getCategories();
    
  }

  getCategories(){
    this.apiService.getCategoriesFromAPI().subscribe((Categories) => {
      this.categories = Categories;
      this.getCategoryTitleFromUrl();
    });
  }

  getCategoryTitleFromUrl(){
    this.route.params.subscribe(params => {
      this.title = params['title'];
      this.category = this.categories.find(category => category.title === this.title);
     this.getSubcategories();

    });
  }

  getSubcategories(){
    this.apiService.getSubcategoriesFromAPI().subscribe((subcategories) => {
      this.subcategories = subcategories;
      this.subcategoriesFromCategory = [];
      for (let key in this.subcategories) {
        if (this.subcategories[key].id_category === this.category.id) {
          this.subcategoriesFromCategory.push(this.subcategories[key]);
        }
      }
      this.processQueryParameters();
    });
  }

  initMap() {
    this.map = L.map('mapid').setView([49.352164, 9.145679], 15);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(this.map);

    L.control.fullscreen({
      position: 'topleft',
      title: 'Im Vollbild anzeigen',
      titleCancel: 'Vollbild verlassen'
    }).addTo(this.map);

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
      //when clicked subcategory is a already selectedSubcategory, remove the subcategory from selectedSubcategory
      let index = this.selectedSubcategories.indexOf(subcategory);
      if (index > -1) {
        this.selectedSubcategories.splice(index, 1);

        //insert the subcategory again in the subcategoriesFromCategory Array at the previous index, only if the matching category is selected
        if (subcategory.id_category == this.category.id) {
          let subcategory_arrayindex = this.subcategoryArrayIndex.find(subcategory_arrayindex => subcategory_arrayindex.subcategory.id == subcategory.id);
          this.subcategoriesFromCategory.splice(subcategory_arrayindex.index, 0, subcategory)
        }
      }

    } else {
     
      //when clicked subcategory is NOT a selectedSubcategory, push the subcategory into selectedSubcategories
      this.selectedSubcategories.push(subcategory);
      let index = this.subcategoriesFromCategory.indexOf(subcategory);
      console.log(index);
      if (index > -1) {
        this.subcategoriesFromCategory.splice(index, 1);
        //save the subcategoryID and the index from the subcategoriesFromCategory to put them back in at the right index later (when subcateory gets unselected again)
        let subcategory_arrayindex: Subcategory_ArrayIndex = { subcategory: subcategory, index: index };
        this.subcategoryArrayIndex.push(subcategory_arrayindex);

        //display the POIs from the given subcategory on map
        this.displayPOIsOnMap(subcategory.id);
      }
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
      let markerArray = [];
      let _this = this;
      let subcategory:Subcategory = this.selectedSubcategories.find(subcategory => subcategory.id == subcategoryID)
      for (let feature of featureCollection.features) {
        if (feature.geometry.type == "Point") {
         
          let marker = L.geoJSON(feature).addTo(this.map).bindPopup("<b>"+subcategory.title+"</b><br>"+feature.properties.title
            + "<br><br> <b>Adresse:</b> <br>" + feature.properties.address.street
            + " " + feature.properties.address.housenumber + "<br>" + feature.properties.address.zipcode
            + " " + feature.properties.address.city
            +"<br> <a href='https://google.de/maps/place/"
            +feature.properties.address.street+" "
            +feature.properties.address.housenumber+", "
            +feature.properties.address.zipcode+" "
            +feature.properties.address.city+"'>Auf Google Maps ansehen</a>")
            .openPopup().on('click', function () {

              _this.setPropertyClassVariablesOnMapClick(feature);
            });
          markerArray.push(marker);
        }
        else if (feature.geometry.type == "Polygon") {

          let marker = L.geoJSON(feature, {
            style: this.polygonStyle
          }).addTo(this.map).bindPopup("<b>"+subcategory.title+"</b><br>"+feature.properties.title)
            .openPopup().on('click', function () {

              _this.setPropertyClassVariablesOnMapClick(feature);
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

  overridePropertyClassVariables() {

    this.setPropertyClassVariablesNull();

    this.properties.forEach(property => {
      if (property instanceof Address) {
        this.address = property;
      }
      else if (property instanceof OpeningHours) {

        this.openingHours = property;
      }
      else if (property instanceof Description) {
        this.description = property;
      }
      else if (property instanceof Price) {
        this.price = property;
      }
      else if (property instanceof Areanumber) {
        this.areanumber = property;
      }
      else if (property instanceof Buildingyear) {
        this.buildingyear = property;
      }
      else if (property instanceof Denomination) {
        this.denomination = property;
      }
      else if (property instanceof Difficulty) {
        this.difficulty = property;
      }
      else if (property instanceof Length) {
        this.length = property;
      }
      else if (property instanceof No_Buildingplaces) {
        this.no_buildingplaces = property;
      }
      else if (property instanceof No_Free_Buildingplaces) {
        this.no_free_buildingplaces = property;
      }
      else if (property instanceof No_Places) {
        this.no_places = property;
      }
      else if (property instanceof School_Type) {
        this.school_type = property;
      }
      else if (property instanceof Using_Type) {
        this.using_type = property;
      }


    });
  }

  checkIfDisplayMapInfo(): boolean {
    if (this.selectedSubcategories.length == 0) {
      this.setPropertyClassVariablesNull();
      return false;
    }
    if (this.selectedSubcategories.length > 0 && (this.description != null
      || this.openingHours != null
      || this.address != null
      || this.price != null
      || this.areanumber != null
      || this.buildingyear != null
      || this.denomination != null
      || this.difficulty != null
      || this.length != null
      || this.no_buildingplaces != null
      || this.no_free_buildingplaces != null
      || this.no_places != null
      || this.school_type != null
      || this.using_type != null)) {
      return true
    }
    return false;
  }

  setPropertyClassVariablesNull() {
    this.price = null;
    this.address = null;
    this.openingHours = null;
    this.description = null;
    this.areanumber = null;
    this.buildingyear = null;
    this.denomination = null;
    this.difficulty = null;
    this.length = null;
    this.no_buildingplaces = null;
    this.no_free_buildingplaces = null;
    this.no_places = null;
    this.school_type = null;
    this.using_type = null;
  }

  setPropertyClassVariablesOnMapClick(feature: Feature) {
    this.properties = [];
    if (feature.properties.openinghours) {

      let openingHours: OpeningHours = new OpeningHours(
        feature.properties.openinghours.monday,
        feature.properties.openinghours.tuesday,
        feature.properties.openinghours.wednesday,
        feature.properties.openinghours.thursday,
        feature.properties.openinghours.friday,
        feature.properties.openinghours.saturday,
        feature.properties.openinghours.sunday);
      this.properties.push(openingHours);
      this.mapInfo = true;
      this.overridePropertyClassVariables();

    }
    if (feature.properties.address) {

      let address: Address = new Address(
        feature.properties.address.street,
        feature.properties.address.housenumber,
        feature.properties.address.zipcode,
        feature.properties.address.city);
      this.properties.push(address);
      this.mapInfo = true;
      this.overridePropertyClassVariables();
    }
    if (feature.properties.price) {
      if (feature.properties.price.length > 0) {
        this.properties.push(new Price(feature.properties.price));
        this.mapInfo = true;
        this.overridePropertyClassVariables();
      }
    }

    if (feature.properties.description) {
      if (feature.properties.description.length > 0) {
        this.properties.push(new Description(feature.properties.description));
        this.mapInfo = true;
        this.overridePropertyClassVariables();
      }
    }
    if (feature.properties.areanumber) {

      this.properties.push(new Areanumber(feature.properties.areanumber));
      this.mapInfo = true;
      this.overridePropertyClassVariables();

    }
    if (feature.properties.buildingyear) {

      this.properties.push(new Buildingyear(feature.properties.buildingyear));
      this.mapInfo = true;
      this.overridePropertyClassVariables();

    }
    if (feature.properties.denomination) {
      if (feature.properties.denomination.length > 0) {
        this.properties.push(new Denomination(feature.properties.denomination));
        this.mapInfo = true;
        this.overridePropertyClassVariables();
      }
    }
    if (feature.properties.difficulty) {
      if (feature.properties.difficulty.length > 0) {
        this.properties.push(new Difficulty(feature.properties.difficulty));
        this.mapInfo = true;
        this.overridePropertyClassVariables();
      }
    }
    if (feature.properties.length) {

      this.properties.push(new Length(feature.properties.length));
      this.mapInfo = true;
      this.overridePropertyClassVariables();

    }
    if (feature.properties.no_buildingplaces) {

      this.properties.push(new No_Buildingplaces(feature.properties.no_buildingplaces));
      this.mapInfo = true;
      this.overridePropertyClassVariables();

    }
    if (feature.properties.no_free_buildingplaces) {

      this.properties.push(new No_Free_Buildingplaces(feature.properties.no_free_buildingplaces));
      this.mapInfo = true;
      this.overridePropertyClassVariables();

    }
    if (feature.properties.no_places) {

      this.properties.push(new No_Places(feature.properties.no_places));
      this.mapInfo = true;
      this.overridePropertyClassVariables();

    }
    if (feature.properties.school_type) {
      if (feature.properties.school_type.length > 0) {
        this.properties.push(new School_Type(feature.properties.school_type));
        this.mapInfo = true;
        this.overridePropertyClassVariables();
      }
    }
    if (feature.properties.using_type) {
      if (feature.properties.using_type.length > 0) {
        this.properties.push(new Using_Type(feature.properties.using_type));
        this.mapInfo = true;
        this.overridePropertyClassVariables();
      }
    }
  }

  toogleHoverAnimation(id: string, element: string, cssClass: string) {
    $("#" + id).find("." + element).toggleClass(cssClass);
  }

  checkOpeningHours(openingHours: any){
    if(!openingHours){
      return false;
    }else if(openingHours.length > 0){
      return true;
    }else{
      return false;
    }
  }

}
