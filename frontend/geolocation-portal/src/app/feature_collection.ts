
export abstract class Geometry{
}
export class Point extends Geometry {
	constructor(
		public type: string,
		public coordinates: number[]
	)
	{super();}
}
export class Polygon extends Geometry {
	constructor(
		public type: string,
		public coordinates: number[][][]
	)
	{super();}
}


export class Feature {
	constructor(
		public type: string,
		public geometry: Geometry,
		public properties: any
	){}
}

export class FeatureCollection {

	constructor(
		public type: string,
		public features: Feature[]
	){
		if(type !== "FeatureCollection")
			throw new Error(`FeatureCollection must have a property 'type' with value 'FeatureCollection', but received 'type': ${type}`);
	}
}
