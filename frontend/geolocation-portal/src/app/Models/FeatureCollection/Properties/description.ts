import { InfoObject } from './infoObject';

export class Description extends InfoObject{
   description: string;
   type: string

   constructor(description: string, type: string){
    super();
    this.type = type;
    this.description = description;
    
   }
}
    