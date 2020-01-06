import { Geometry } from './geometry';
import { Property } from './property';

export class Feature{
    type: string;
    geometry: Geometry;
    properties: Property;
     }