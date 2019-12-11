import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Subcategory } from './subcategory';
import { SUBCATEGORIES } from './api-data';

@Injectable({
  providedIn: 'root'
})
export class SubcategoryService {

  constructor() { }

  getSubcategories(): Observable<Subcategory[]>{
    return of(SUBCATEGORIES);
  }
}
