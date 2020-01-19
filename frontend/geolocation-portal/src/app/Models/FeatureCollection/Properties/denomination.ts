import { InfoObject } from './infoObject';

export class Denomination extends InfoObject{
  denomination: string;


  constructor(denomination:string){
    super();
      this.denomination = denomination;
  }
}
    