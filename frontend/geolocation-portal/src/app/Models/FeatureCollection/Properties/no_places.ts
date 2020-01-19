import { InfoObject } from './infoObject';

export class No_Places extends InfoObject{
  no_places: number;


  constructor(no_places:number){
    super();
      this.no_places = no_places;
  }
}
    