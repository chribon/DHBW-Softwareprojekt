import { Category } from './category';
import { Subcategory } from './subcategory';
import { Entry } from './entry';

export const CATEGORIES: Category[] = [
  { id: 1, title: 'Wohnen' , description: "test"},
  { id: 2, title: 'Müllentsorgung', description:"test" },
];


export const SUBCATEGORIES: Subcategory[] = [
  { id: 1, cid: 1, title: 'Wohngebiete', type:'"map' },
  { id: 2, cid: 2, title: 'Mülleimer', type:'map' },
  { id: 3, cid: 2, title: 'test', type:'map' },
];
export const ENTRIES: Entry[] = [
  {id: 1, title: "mülleimer 1", content: [{lat:49.346881, long: 9.135313 }]},
  {id: 1, title: "mülleimer 1", content: [{lat:49.358234,  long:9.148750}]}
]