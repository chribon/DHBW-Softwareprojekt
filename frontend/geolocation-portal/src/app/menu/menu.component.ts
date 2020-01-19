import { Component, OnInit} from '@angular/core';
import { Category } from '../Models/category';
import { Subcategory } from '../Models/subcategory';
import { APIService } from '../api.service';


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
  searchRegex: RegExp;
  
  constructor(private apiSerivce: APIService) { }

  ngOnInit() {
    this.getCategories();
    this.getSubcategories();
  }

  search(){
    this.searchCategories = [];
    this.searchTermLength = this.searchTerm.length;
    this.searchRegex = new RegExp(this.searchTerm, "i");
    for (let category of this.categories) {
     
      if (category.title.match(this.searchRegex) && this.searchTerm.length != 0) {
        this.searchCategories.push(category);
      }
    }
    for (let subcategory of this.subcategories) {
     
      if (subcategory.title.match(this.searchRegex) && this.searchTerm.length != 0) {

        if(!(this.searchCategories.some(category => category.id == subcategory.id_category))){
          this.searchCategories.push(this.categories.find(category => category.id == subcategory.id_category));
        }
        
      }
    }

    this.searchCategoriesLength = this.searchCategories.length;
  }

  getSubcategories(){
    this.apiSerivce.getSubcategoriesFromAPI().subscribe((subcategories) => (this.subcategories = subcategories));
  }

  getCategories(){
    this.apiSerivce.getCategoriesFromAPI().subscribe((category) => (this.categories = category));
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
}
