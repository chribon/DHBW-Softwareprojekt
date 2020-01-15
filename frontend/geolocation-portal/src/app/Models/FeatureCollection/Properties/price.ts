import { InfoObject } from './infoObject';

export class Price extends InfoObject{
  price: string;
  type: string;

  constructor(price: string, type:string){
    super();
    this.type = type;
      this.price = price;
  }
}
    