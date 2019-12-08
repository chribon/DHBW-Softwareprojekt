import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MenuComponent } from './menu/menu.component';
import { MapComponent } from './map/map.component';


const routes: Routes = [
  {path: '', redirectTo: '/menu', pathMatch: 'full'},
  {path: 'menu', component: MenuComponent},
  {path: 'map', component: MapComponent},
  {path: 'map/:id', component: MapComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
