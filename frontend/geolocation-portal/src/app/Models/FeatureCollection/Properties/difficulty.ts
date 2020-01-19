import { InfoObject } from './infoObject';

export class Difficulty extends InfoObject{
  difficulty: string;


  constructor(difficulty:string){
    super();
      this.difficulty = difficulty;
  }
}
    