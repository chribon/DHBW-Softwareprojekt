import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MenuComponent } from './menu/menu.component';
import { MapComponent } from './map/map.component';
import { MapNavComponent } from './map-nav/map-nav.component';
import { ApiComponent } from './api/api.component';
import { VorschlagComponent } from './vorschlag/vorschlag.component';


const routes: Routes = [
  {path: '', redirectTo: '/menu', pathMatch: 'full'},
  {path: 'menu', component: MenuComponent},
  {path: 'api', component: ApiComponent},
  {path: 'vorschlaege_einreichen', component: VorschlagComponent},
  {path: 'map', component: MapNavComponent,  children: [
    {path: ':title', component:MapComponent}
    ]}
 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
