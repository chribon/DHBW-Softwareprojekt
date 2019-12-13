import { Component, OnInit } from '@angular/core';
import { Category } from '../category';
import { CategoryService } from '../category.service';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { SubcategoryService } from '../subcategory.service';
import { Subcategory } from '../subcategory';



@Component({
  selector: 'app-map-nav',
  templateUrl: './map-nav.component.html',
  styleUrls: ['./map-nav.component.css']
})
export class MapNavComponent implements OnInit {

  category: Category;
  categories: Category[];
 

  constructor(private route: ActivatedRoute,
    private categoryService: CategoryService,
    private subcategoryService: SubcategoryService,
    private location: Location, ) { }

  ngOnInit() {
    this.getCategory();
    this.getCategories();

  }

  getCategory(): void {
    const title = this.route.snapshot.paramMap.get('title');

    this.categoryService.getCategoryByTitle(title).subscribe(category => (this.category = category));

  }
  getCategories(): void {
    this.categoryService.getCategories().subscribe(Category => (this.categories = Category));
  }

  
  
}