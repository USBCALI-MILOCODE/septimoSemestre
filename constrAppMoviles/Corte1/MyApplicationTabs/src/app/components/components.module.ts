import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PersonajesComponent } from './personajes/personajes.component';
import { IonicModule } from '@ionic/angular';
import { LugaresComponent } from './lugares/lugares.component';
import { FavoritesComponent } from './favorites/favorites.component';
import { SearchComponent } from './search/search.component';



@NgModule({
  declarations: [
    PersonajesComponent,
    LugaresComponent,
    FavoritesComponent,
    SearchComponent
  ],
  imports: [
    CommonModule,
    IonicModule
  ],
  exports: [
    PersonajesComponent,
    LugaresComponent,
    FavoritesComponent,
    SearchComponent
  ]
})
export class ComponentsModule { }
