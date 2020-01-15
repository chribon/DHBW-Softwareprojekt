import { InfoObject } from './infoObject';

export class Adress extends InfoObject{
    street: string;
    housenumber: number;
    zipcode: number;
    city: string;

    
    constructor(street: string, housenumber: number, zipcode: number, city: string){
        super();
  
        this.street = street;
        this.housenumber = housenumber;
        this.zipcode = zipcode;
        this.city = city;
       
      }
     }