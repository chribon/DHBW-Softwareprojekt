import { InfoObject } from './infoObject';

export class Description extends InfoObject{
   description: string;

   constructor(description: string, type: string){
    super();
    this.description = description;
    
   }
}
    