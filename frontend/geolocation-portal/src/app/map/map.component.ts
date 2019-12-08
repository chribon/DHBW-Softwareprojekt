import { Component, OnInit } from '@angular/core';
import { Category} from '../category';
import { CategoryService} from '../category.service';
import { ActivatedRoute } from '@angular/router';
import {Location} from '@angular/common';


@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {
category: Category;
  constructor(private route:ActivatedRoute, 
    private categoryService: CategoryService,
    private location: Location,) { }

  ngOnInit() {
    this.getCategory();
  }

  getCategory(): void{
    const id = +this.route.snapshot.paramMap.get('id');

    this.categoryService.getCategory(id).subscribe(category =>( this.category = category));

  }
}
