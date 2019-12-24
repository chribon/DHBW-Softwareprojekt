import { Injectable } from '@angular/core';
import { Category } from './category';
import { CATEGORIES } from './api-data';
import { Observable, of } from 'rxjs';
import { MessageService } from './message.service';

@Injectable({
  providedIn: 'root'
})
export class CategoryService {

  constructor(private messageService: MessageService) { }

  getCategories(): Observable<Category[]> {
    this.messageService.add('Categoires fetched');
    return of( CATEGORIES);
  }

  getCategoryByTitle(title: string): Observable<Category>{
    this.messageService.add('Category fetched');
    return of(CATEGORIES.find(category =>( category.title === title)));
  }
}
