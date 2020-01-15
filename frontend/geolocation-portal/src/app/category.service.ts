import { Injectable } from '@angular/core';
import { Category } from './category';
//import { CATEGORIES } from './testdata';
import { Observable, of } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class CategoryService {
 
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
  constructor( private http: HttpClient) { 

    
  }

  getCategoriesFromAPI(): Observable<Category[]>{
    return this.http.get<Category[]>("http://127.0.0.1:8000/api/categories/").pipe(
      catchError(this.handleError<Category[]>('getCategoriesFromAPI', []))
    );
  }

  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(error); 
      return of(result as T);
    };
  }

/* alte Funktionen ohne API

  getCategories(): Observable<Category[]> {
    this.messageService.add('Categoires fetched');
    return of( CATEGORIES);
  }

   getCategoryByTitle(title: string): Observable<Category>{
    this.messageService.add('Category fetched');
    return of(CATEGORIES.find(category =>( category.title === title)));
  }  */
 

}
