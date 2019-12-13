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

  getSubcategoriesFilterByCid(cid: number): Observable<Subcategory[]>{
    
    let Subcategories = [];
    for(let key in SUBCATEGORIES){
      if(SUBCATEGORIES[key].cid === cid ){
        Subcategories.push(SUBCATEGORIES[key]);
      }
    }
    return of(Subcategories);
  }
}
