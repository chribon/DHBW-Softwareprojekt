import { InfoObject } from './infoObject';

export class Buildingyear extends InfoObject{
  buildingyear: number;


  constructor(buildingyear:number){
    super();
      this.buildingyear = buildingyear;
  }
}
    