import { InfoObject } from './infoObject';

export class Price extends InfoObject{
  price: string;


  constructor(price: string, type:string){
    super();
      this.price = price;
  }
}
    