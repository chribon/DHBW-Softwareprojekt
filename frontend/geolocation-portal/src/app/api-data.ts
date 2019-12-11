import { Category } from './category';
import { Subcategory } from './subcategory';

export const CATEGORIES: Category[] = [
  { id: 1, name: 'Wohnen' },
  { id: 2, name: 'Müllentsorgung' },
];


export const SUBCATEGORIES: Subcategory[] = [
  { id: 1, cid: 1, name: 'Wohngebiete' },
  { id: 2, cid: 2, name: 'Mülleimer' },
  { id: 3, cid: 2, name: 'test' },
];
