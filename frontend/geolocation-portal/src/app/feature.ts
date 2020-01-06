import { Coordinate } from './coordinate';
import { Property } from './property';

export class Feature{
    type: string;
    geometry: Coordinate;
    properties: Property;
     }