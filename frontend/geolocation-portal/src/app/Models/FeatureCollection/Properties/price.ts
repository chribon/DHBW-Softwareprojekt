import { InfoObject } from './infoObject';

export class Price extends InfoObject{
  price: string;


  constructor(price: string){
    super();
      this.price = price;
  }
}
    