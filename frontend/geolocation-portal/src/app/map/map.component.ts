import { Component, OnInit } from '@angular/core';
import { Category } from '../category';
import { CategoryService } from '../category.service';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { SubcategoryService } from '../subcategory.service';
import { Subcategory } from '../subcategory';
import * as L from 'leaflet';


@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {
  category: Category;
  subcategories: Subcategory[];


  constructor(private route: ActivatedRoute,
    private categoryService: CategoryService,
    private subcategoryService: SubcategoryService,
    private location: Location, ) { }

  ngOnInit() {
    this.getCategory();
    this.getSubcategories();
    this.initMap();
  }

  getCategory(): void {
    const id = +this.route.snapshot.paramMap.get('id');

    this.categoryService.getCategory(id).subscribe(category => (this.category = category));

  }
  getSubcategories(): void {
    this.subcategoryService.getSubcategories().subscribe(Subcategory => (this.subcategories = Subcategory));
  }

  filterCategoryOf(cid: number): Subcategory[] {
    return this.subcategories.filter(Subcategory => Subcategory.cid = cid);
  }
  initMap() {
    const map = L.map('mapid').setView([49.352164, 9.145679], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    var greenIcon = L.icon({
      iconUrl: 'assets/marker-icon.png',
      shadowUrl: 'assets/marker-shadow.png',
  
      iconSize:     [38, 95], // size of the icon
      shadowSize:   [50, 64], // size of the shadow
      iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
      shadowAnchor: [4, 62],  // the same for the shadow
      popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
  });

  L.marker([49.354315, 9.150179], {icon: greenIcon}).addTo(map).bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
  .openPopup();
    
  }
}
