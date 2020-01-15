import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Subcategory } from './Models/subcategory';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError} from 'rxjs/operators';
import { FeatureCollection } from './Models/FeatureCollection/featurecollection';
import { Category } from './Models/category';

@Injectable({
  providedIn: 'root'
})
export class APIService {

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(private http: HttpClient) { }

  getCategoriesFromAPI(): Observable<Category[]> {
    return this.http.get<Category[]>("http://127.0.0.1:8000/api/categories/").pipe(
      catchError(this.handleError<Category[]>('getCategoriesFromAPI', []))
    );
  }

  getSubcategoriesFromAPI(): Observable<Subcategory[]> {
    return this.http.get<Subcategory[]>("http://127.0.0.1:8000/api/subcategories/").pipe(
      catchError(this.handleError<Subcategory[]>('getSubcategoriesFromAPI', []))
    );
  }

  getEntriesFromAPI(subcategoryID: number): Observable<FeatureCollection> {
    return this.http.get<FeatureCollection>("http://127.0.0.1:8000/api/subcategories/" + subcategoryID + "/entries/").pipe(
      catchError(this.handleError<FeatureCollection>('getEntriesFromAPI', null))
    );
  }


  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(error);
      return of(result as T);
    };
  }
}
