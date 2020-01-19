import { Component, OnInit } from '@angular/core';
import { Category } from '../Models/category';
import { ActivatedRoute } from '@angular/router';
import * as $ from 'jquery';
import { APIService } from '../api.service';


@Component({
  selector: 'app-map-nav',
  templateUrl: './map-nav.component.html',
  styleUrls: ['./map-nav.component.css']
})
export class MapNavComponent implements OnInit {

  categories: Category[];
  category: Category;
  title: string;


  constructor(private route: ActivatedRoute,
     private apiService: APIService) { }

  ngOnInit() {
    this.getCategories();
  }

  getCategories(){
    this.apiService.getCategoriesFromAPI().subscribe(categories => {
      this.categories = categories;

      this.getCategoryTitleFromUrl();
    });
  }
  
  getCategoryTitleFromUrl(){
    this.route.firstChild.params.subscribe(params => {
      this.title = params['title'];
        this.category = this.categories.find(category => category.title === this.title);
      });
  }

}