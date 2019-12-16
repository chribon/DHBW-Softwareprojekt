import { Category } from './category';
import { Subcategory } from './subcategory';
import { Entry } from './entry';

export const CATEGORIES: Category[] = [
  { id: 1, title: 'kategorie1' , description:"test"},
  { id: 2, title: 'kategorie2', description:"test" },
  { id: 3, title: 'kategorie3', description:"test" },
  { id: 4, title: 'kategoryie', description:"test" },
  { id: 5, title: 'kategorie5', description:"test" },
  { id: 6, title: 'kategorie6', description:"test" },
];


export const SUBCATEGORIES: Subcategory[] = [
  { id: 1, cid: 1, title: 'subcategorie1.1', type:'"map' },
  { id: 2, cid: 1, title: 'subcategorie1.2', type:'"map' },
  { id: 3, cid: 2, title: 'subcategorie2.1', type:'map' },
  { id: 4, cid: 2, title: 'subcategorie2.2', type:'map' },
  { id: 5, cid: 3, title: 'subcategorie3.1', type:'map' },
  { id: 6, cid: 3, title: 'subcategorie3.2', type:'map' },
];
export const ENTRIES: Entry[] = [
  {id: 1, title: "mülleimer 1", content: [{lat:49.346881, long: 9.135313 }]},
  {id: 1, title: "mülleimer 1", content: [{lat:49.358234,  long:9.148750}]}
]