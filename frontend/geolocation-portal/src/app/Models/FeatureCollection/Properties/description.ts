import { InfoObject } from './infoObject';

export class Description extends InfoObject{
   description: string;

   constructor(description: string){
    super();
    this.description = description;
    
   }
}
    