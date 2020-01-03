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

  search(): void {
    this.searchCategories = [];
    this.searchTermLength = this.searchTerm.length;

    for (let category of this.categories) {
      if (category.title.includes(this.searchTerm) && this.searchTerm.length != 0) {
        this.searchCategories.push(category);
      }
    }
    for (let subcategory of this.subcategories) {
      if (subcategory.title.includes(this.searchTerm) && this.searchTerm.length != 0) {
        this.searchCategories.push(this.categories.find(category => category.id == subcategory.cid));
      }
    }

    this.searchCategoriesLength = this.searchCategories.length;
  }

  getSubcategories(): void {
    this.subcategoryService.getSubcategories().subscribe(Subcategory => (this.subcategories = Subcategory));
  }
  getCategories(): void {
    this.categoryService.getCategories().subscribe(CATEGORIES => (this.categories = CATEGORIES));
  }
  getSubcategoriesOfCatgory(category: Category): Subcategory[] {
    let subcategories: Subcategory[];
    for (let subcategory of this.subcategories) {
      if (category.id == subcategory.cid) {
        this.subcategories.push(subcategory);
      }
    }
    return subcategories;
  }

}
