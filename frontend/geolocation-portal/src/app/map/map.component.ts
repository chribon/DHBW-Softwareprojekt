import { Component, OnInit } from '@angular/core';
import { Category } from '../category';
import { CategoryService } from '../category.service';
import { ActivatedRoute } from '@angular/router';
import { SubcategoryService } from '../subcategory.service';
import { Subcategory } from '../subcategory';
import * as L from 'leaflet';
import { REFERENCE_PREFIX } from '@angular/compiler/src/render3/view/util';


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
  sub: any;
  title: string;
  selectedSubcategories: Subcategory[] = [];

  constructor(private route: ActivatedRoute,
    private categoryService: CategoryService,
    private subcategoryService: SubcategoryService) { }

  ngOnInit() {
    this.initMap();
    this.categoryService.getCategoriesFromAPI().subscribe((Categories) => {
    this.categories = Categories;

      this.sub = this.route.params.subscribe(params => {
        this.title = params['title'];
        this.category = this.categories.find(category => category.title === this.title);
        this.subcategoryService.getSubcategoriesFromAPI().subscribe((subcategories) => {

          this.subcategories = subcategories;
          this.subcategoriesFromCategory = [];
          for (let key in this.subcategories) {
            if (this.subcategories[key].id_category === this.category.id) {
              this.subcategoriesFromCategory.push(this.subcategories[key]);
            }
          }

        });

      });

    });

    /* this.getCategory();
    this.getSubcategories();
    this.initMap();
    this.sub = this.route.params.subscribe(params => {
      this.title = params['title'];
      this.categoryService.getCategoryByTitle(this.title).subscribe(category => (this.category = category));
      this.subcategoryService.getSubcategoriesFilterByCid(this.category.id).subscribe(subcategories => (this.subcategories = subcategories));
    });  */

  }
  ngOnDestroy() {
    this.sub.unsubscribe();
  }


  initMap() {
    const map = L.map('mapid').setView([49.352164, 9.145679], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    var greenIcon = L.icon({
      iconUrl: 'assets/marker-icon.png',
      shadowUrl: 'assets/marker-shadow.png',

      iconSize: [38, 95], // size of the icon
      shadowSize: [50, 64], // size of the shadow
      iconAnchor: [22, 94], // point of the icon which will correspond to marker's location
      shadowAnchor: [4, 62],  // the same for the shadow
      popupAnchor: [-3, -76] // point from which the popup should open relative to the iconAnchor
    });

    L.marker([49.354315, 9.150179], { icon: greenIcon }).addTo(map).bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
      .openPopup();

  }

  toggleSubcategory(subcategory: Subcategory) {

    if (this.selectedSubcategories.some(subcategoryFromArray => subcategoryFromArray.title === subcategory.title)) {
      var index = this.selectedSubcategories.indexOf(subcategory);
      if (index > -1) {
        this.selectedSubcategories.splice(index, 1);
      }
    } else {
      this.selectedSubcategories.push(subcategory);
    }
    console.log(this.selectedSubcategories);

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



   /* alte Funktionen ohne API
  
  getCategory(): void {
    const title = this.route.snapshot.paramMap.get('title');

    this.categoryService.getCategoryByTitle(title).subscribe(category => (this.category = category));

  }
 getSubcategories(): void {
    this.subcategoryService.getSubcategories().subscribe(Subcategory => (this.subcategories = Subcategory));
  }  */



}
