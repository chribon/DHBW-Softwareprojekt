import { Component, OnInit } from '@angular/core';
import { SubcategoryService } from '../subcategory.service';
import { FeatureCollection, Feature, GroundValueProperties } from '../feature_collection';

@Component({
  selector: 'app-impressum',
  templateUrl: './impressum.component.html',
  styleUrls: ['./impressum.component.css']
})
export class ImpressumComponent implements OnInit {
	featureCollection: FeatureCollection;
	featureCollectionAsString: string;
	isLoaded: boolean;
	property: GroundValueProperties;
	propertyAsString: string;

	constructor(
		private subcategoryService: SubcategoryService) { }

	ngOnInit() {
		this.isLoaded = false;
		this.getSubcategoryOneEntries();
	}
	
	getSubcategoryOneEntries(){
		this.subcategoryService.getEntriesFromAPI(7)
			.subscribe(featureCollection => {
				this.isLoaded = true;
				this.featureCollection = featureCollection;
				this.featureCollectionAsString = JSON.stringify(featureCollection);
				this.property = this.featureCollection.features[0].properties as GroundValueProperties;
				this.propertyAsString = JSON.stringify(this.property);
				// auch type checks funktionieren so
				this.property.price; // kein Compiler-Fehler
				//this.property.pprice; // Compiler-Fehler
			});
	}
}
