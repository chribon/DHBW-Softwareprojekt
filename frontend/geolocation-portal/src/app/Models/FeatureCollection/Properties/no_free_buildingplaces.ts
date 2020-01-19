import { InfoObject } from './infoObject';

export class No_Free_Buildingplaces extends InfoObject{
  no_free_buildingplaces: number;


  constructor(no_free_buildingplaces:number){
    super();
      this.no_free_buildingplaces = no_free_buildingplaces;
  }
}
    