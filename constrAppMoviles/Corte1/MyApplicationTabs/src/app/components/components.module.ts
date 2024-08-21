import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PersonajesComponent } from './personajes/personajes.component';
import { IonicModule } from '@ionic/angular';
import { LugaresComponent } from './lugares/lugares.component';
import { FavoritesComponent } from './favorites/favorites.component';



@NgModule({
  declarations: [
    PersonajesComponent,
    LugaresComponent,
    FavoritesComponent
  ],
  imports: [
    CommonModule,
    IonicModule
  ],
  exports: [
    PersonajesComponent,
    LugaresComponent,
    FavoritesComponent
  ]
})
export class ComponentsModule { }
