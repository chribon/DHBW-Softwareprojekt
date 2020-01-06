
export abstract class Geometry {
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


export class Properties {
	constructor(
		public title: string
	){}
}

export class GroundValueProperties extends Properties {
	constructor(
		public title: string,
		public price: string
	)
	{
		super(title);
		price += "toller Preis";
	}
}

export class GlassTrashProperties extends Properties {
	public openingHours: string
	constructor(
		public title: string,
	){ super(title); }
}


export class Feature {
	constructor(
		public type: string,
		public geometry: Geometry,
		public properties: Properties
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
