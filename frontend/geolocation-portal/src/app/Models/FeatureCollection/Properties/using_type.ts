import { InfoObject } from './infoObject';

export class Using_Type extends InfoObject{
  using_type: string;


  constructor(using_type:string){
    super();
      this.using_type = using_type;
  }
}
    