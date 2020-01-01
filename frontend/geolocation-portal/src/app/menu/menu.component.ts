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

  constructor(private categoryService: CategoryService,
    private subcategoryService: SubcategoryService) { }

  searchTerm: string;

  ngOnInit() {
    this.getCategories();
    this.getSubcategories();
  }

  search() {
    this.searchCategories = [];
    for (let category of this.categories) {
      if (category.title.includes(this.searchTerm)) {
        this.searchCategories.push(category);
      }
    }
    for (let subcategory of this.subcategories) {
      if (subcategory.title.includes(this.searchTerm)) {
        this.searchCategories.push(this.categories.find(category => category.id == subcategory.cid));
      }
    }
    console.log(this.searchCategories);

  }

  getSubcategories(): void {
    this.subcategoryService.getSubcategories().subscribe(Subcategory => (this.subcategories = Subcategory));
  }
  getCategories() {
    this.categoryService.getCategories().subscribe(CATEGORIES => (this.categories = CATEGORIES));
  }

}
