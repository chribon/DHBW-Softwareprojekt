import { Component, OnInit } from '@angular/core';
import { CategoryService } from '../category.service';
import { Category } from '../category';
import { Subcategory } from '../subcategory';
import { SubcategoryService } from '../subcategory.service';



@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {

  categories: Category[];
  subcategories: Subcategory[];
  searchCategories: Category[];
  searchCategoriesLength: number;
  searchTerm: string;
  searchTermLength: number;
  constructor(private categoryService: CategoryService,
    private subcategoryService: SubcategoryService) { }



  ngOnInit() {
    this.getCategories();
    this.getSubcategories();
  }

  search(){
    this.searchCategories = [];
    this.searchTermLength = this.searchTerm.length;

    for (let category of this.categories) {
      if (category.title.includes(this.searchTerm) && this.searchTerm.length != 0) {
        this.searchCategories.push(category);
      }
    }
    for (let subcategory of this.subcategories) {
      if (subcategory.title.includes(this.searchTerm) && this.searchTerm.length != 0) {

        if(!(this.searchCategories.some(category => category.id == subcategory.id_category))){
          this.searchCategories.push(this.categories.find(category => category.id == subcategory.id_category));
        }
        
      }
    }

    this.searchCategoriesLength = this.searchCategories.length;
  }

  getSubcategories(){
    this.subcategoryService.getSubcategoriesFromAPI().subscribe((subcategories) => (this.subcategories = subcategories));
  }
  getCategories(){
    this.categoryService.getCategoriesFromAPI().subscribe((category) => (this.categories = category));
  }
  getSubcategoriesOfCatgory(category: Category): Subcategory[] {
    let subcategories: Subcategory[];
    for (let subcategory of this.subcategories) {
      if (category.id == subcategory.id_category) {
        this.subcategories.push(subcategory);
      }
    }
    return subcategories;
  }



   /* alte Funktionen ohne API
  
  getSubcategories(){
    this.subcategoryService.getSubcategories().subscribe(Subcategory => (this.subcategories = Subcategory));
  }
  getCategories(){
    this.categoryService.getCategories().subscribe(CATEGORIES => (this.categories = CATEGORIES));
  } */

}
