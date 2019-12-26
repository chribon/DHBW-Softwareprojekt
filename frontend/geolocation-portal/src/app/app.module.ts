import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { MapComponent } from './map/map.component';
import { ApiComponent } from './api/api.component';
import { StatisticsComponent } from './statistics/statistics.component';
import { MenuComponent } from './menu/menu.component';
import { SubcategoriesPipe } from './subcategories.pipe';
import { MDBBootstrapModule } from 'angular-bootstrap-md';
import { MapNavComponent } from './map-nav/map-nav.component';
import { VorschlagComponent } from './vorschlag/vorschlag.component';



@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    MapComponent,
    ApiComponent,
    StatisticsComponent,
    MenuComponent,
    SubcategoriesPipe,
    MapNavComponent,
    VorschlagComponent,
 
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MDBBootstrapModule.forRoot()
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
