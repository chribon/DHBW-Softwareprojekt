import { InfoObject } from './infoObject';
import { ThrowStmt } from '@angular/compiler';

export class OpeningHours extends InfoObject
{
    monday: number[];
    tuesday: number[];
    wednesday: number[];
    thursday: number[];
    friday: number[];
    saturday: number[];
    sunday: number[];

    constructor(monday: number[], tuesday: number[], wednesday: number[], thursday: number[], friday: number[],saturday: number[], sunday: number[]){
      super();

      this.monday = monday;
      this.tuesday = tuesday;
      this.wednesday = wednesday;
      this.thursday = thursday;
      this.friday = friday;
      this.saturday = saturday;
      this.sunday = sunday;
    }
  }
  
  