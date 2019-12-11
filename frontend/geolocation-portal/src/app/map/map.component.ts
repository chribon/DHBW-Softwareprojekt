import { Component, OnInit } from '@angular/core';
import { Category} from '../category';
import { CategoryService} from '../category.service';
import { ActivatedRoute } from '@angular/router';
import {Location} from '@angular/common';
import { SubcategoryService } from '../subcategory.service';
import { Subcategory } from '../subcategory';
import { SUBCATEGORIES } from '../api-data';


@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {
category: Category;
subcategories: Subcategory[];


  constructor(private route:ActivatedRoute, 
    private categoryService: CategoryService,
    private subcategoryService:SubcategoryService,
    private location: Location,) { }

  ngOnInit() {
    this.getCategory();
    this.getSubcategories();
  }

  getCategory(): void{
    const id = +this.route.snapshot.paramMap.get('id');

    this.categoryService.getCategory(id).subscribe(category =>( this.category = category));

  }
  getSubcategories(): void{
    this.subcategoryService.getSubcategories().subscribe(Subcategory=>( this.subcategories = Subcategory));
  }

  filterCategoryOf(cid: number): Subcategory[]{
    return this.subcategories.filter(Subcategory => Subcategory.cid = cid);
  }
}
