import { Category } from './category';
import { Subcategory } from './subcategory';
import { Entry } from './entry';

export const CATEGORIES: Category[] = [
  { id: 1, title: 'category1' , description:"test"},
  { id: 2, title: 'category2', description:"test" },
  { id: 3, title: 'category3', description:"test" },
  { id: 4, title: 'category4', description:"test" },
  { id: 5, title: 'category5', description:"test" },
  { id: 6, title: 'category6', description:"test" },
];


export const SUBCATEGORIES: Subcategory[] = [
  { id: 1, cid: 1, title: 'subcategory1.1', type:'"map' },
  { id: 2, cid: 1, title: 'subcategory1.2', type:'"map' },
  { id: 3, cid: 2, title: 'subcategory2.1', type:'map' },
  { id: 4, cid: 2, title: 'subcategory2.2', type:'map' },
  { id: 5, cid: 3, title: 'subcategory3.1', type:'map' },
  { id: 6, cid: 3, title: 'subcategory3.2', type:'map' },
];
export const ENTRIES: Entry[] = [
  {id: 1, title: "mülleimer 1", content: [{lat:49.346881, long: 9.135313 }]},
  {id: 1, title: "mülleimer 1", content: [{lat:49.358234,  long:9.148750}]}
]