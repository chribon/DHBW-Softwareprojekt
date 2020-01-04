import { Component, OnInit } from '@angular/core';
import { Category } from '../category';
import { CategoryService } from '../category.service';
import { ActivatedRoute } from '@angular/router';
import { SubcategoryService } from '../subcategory.service';
import { Subcategory } from '../subcategory';
import * as $ from 'jquery';


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
    private categoryService: CategoryService,
    private subcategoryService: SubcategoryService) { }

  ngOnInit() {

    this.categoryService.getCategoriesFromAPI().subscribe(categories => {
      this.categories = categories;

      this.route.firstChild.params.subscribe(params => {
      this.title = params['title'];

        this.category = this.categories.find(category => category.title === this.title);
      });

    });
  }

  checkSelectedCategoryTitle(): string {
    return this.title;
  }

  /*  alte Funktion ohne API
  
  getCategory(): void {
    this.route.firstChild.params.subscribe(params => {
    this.title = params['title'];

      this.categoryService.getCategoryByTitle(this.title).subscribe(category => (this.category = category));
    });
  }

  getCategories(): void {
     this.categoryService.getCategories().subscribe(Category => (this.categories = Category));
   }  */




}