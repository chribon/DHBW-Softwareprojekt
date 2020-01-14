import { Category } from './category';
import { Subcategory } from './subcategory';


export const CATEGORIES: Category[] = [
  { id: 1, title: 'category1' , description:"test", image: "test"},
  { id: 2, title: 'category2', description:"test",  image: "test" },
  { id: 3, title: 'category3', description:"test",  image: "test" },
  { id: 4, title: 'category4', description:"test",  image: "test"},
  { id: 5, title: 'category5', description:"test",  image: "test"},
  { id: 6, title: 'category6', description:"test",  image: "test"},
];


export const SUBCATEGORIES: Subcategory[] = [
  { id: 1, id_category: 1, title: 'subcategory1.1', description: "test" , entry_types: "test" },
  { id: 2, id_category: 1, title: 'subcategory1.2', description: "test" , entry_types: "test" },
  { id: 3, id_category: 2, title: 'subcategory2.1', description: "test" , entry_types: "test" },
  { id: 4, id_category: 2, title: 'subcategory2.2', description: "test" , entry_types: "test"},
  { id: 5, id_category: 3, title: 'subcategory3.1', description: "test" , entry_types: "test" },
  { id: 6, id_category: 3, title: 'subcategory3.2', description: "test" , entry_types: "test" },
];
