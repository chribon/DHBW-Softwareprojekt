import { Pipe, PipeTransform } from '@angular/core';
import { Subcategory } from './subcategory';

@Pipe({
  name: 'subcategories'
})
export class SubcategoriesPipe implements PipeTransform {

  transform(subcategories: Subcategory, cid: any): any {

    let values = [];
    for(let key in subcategories){
      if(subcategories[key].cid === cid ){
        values.push(subcategories[key]);
      }
    }
    return values;
  }

}
