import { InfoObject } from './infoObject';

export class School_Type extends InfoObject{
  school_type: string;


  constructor(school_type:string){
    super();
      this.school_type= school_type;
  }
}
    