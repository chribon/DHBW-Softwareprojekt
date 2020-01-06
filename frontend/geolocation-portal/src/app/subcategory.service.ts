import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Subcategory } from './subcategory';
import { SUBCATEGORIES } from './api-data';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';
//import { Entry } from './entry';
import { FeatureCollection } from './feature_collection';

@Injectable({
  providedIn: 'root'
})
export class SubcategoryService {

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(private http: HttpClient) { }


  getSubcategoriesFromAPI() {
    return this.http.get<Subcategory[]>("http://127.0.0.1:8000/api/subcategories/").pipe(
      catchError(this.handleError<Subcategory[]>('getSubcategoriesFromAPI', []))
    );
  }

	getEntriesFromAPI(subcategoryID: number): Observable<any>{
    return this.http.get<FeatureCollection>("http://127.0.0.1:8000/api/subcategories/"+subcategoryID+"/entries/").pipe(
	    catchError(this.handleError<FeatureCollection>('getEntriesFromAPI', null))
    );
  }


  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(error);
      return of(result as T);
    };
  }



  /*   alte Funltionen ohne API
  
  
  getSubcategories(): Observable<Subcategory[]>{
      return of(SUBCATEGORIES);
  }
  
  getSubcategoriesFilterByCid(cid: number): Observable<Subcategory[]>{
      
      let Subcategories = [];
      for(let key in SUBCATEGORIES){
        if(SUBCATEGORIES[key].id_category === cid ){
          Subcategories.push(SUBCATEGORIES[key]);
        }
      }
      return of(Subcategories);
    }
    getSubcategoryFilterByTitle(title: string): Observable<Subcategory>{
      
      for(let key in SUBCATEGORIES){
        if(SUBCATEGORIES[key].title === title ){
          return of(SUBCATEGORIES[key]);
        }
      }
      
    } */

}
