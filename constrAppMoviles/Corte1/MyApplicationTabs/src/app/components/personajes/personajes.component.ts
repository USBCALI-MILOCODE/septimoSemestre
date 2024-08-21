import { Component, OnInit, Renderer2 } from '@angular/core';
import { FavoritesService } from 'src/app/services/favorites.service';
import { RickyMortyServiceService } from 'src/app/services/ricky-morty-service.service';

@Component({
  selector: 'app-personajes',
  templateUrl: './personajes.component.html',
  styleUrls: ['./personajes.component.scss'],
})
export class PersonajesComponent implements OnInit {

  personaje: any;  // Variable para almacenar los detalles del personaje seleccionado
  personajesList: any = [];
  iconNames: string[] = [];
  isModalOpen = false;  // Variable para controlar la visibilidad del modal
  updateFavorites: any;

  constructor(
    private _rickyMortyService: RickyMortyServiceService,
    private renderer: Renderer2,
    private _favoritesService: FavoritesService
  ) { }

  ngOnInit() {
    this.getAllCharacters();
  }

  getAllCharacters() {
    this._rickyMortyService.getAllCharacters()
      .then(data => {
        this.personajesList = data;
        this.iconNames = this.personajesList.map((personaje: { id: number; }) =>
          this.isFavorite(personaje.id) ? 'star' : 'star-outline'
        );
      });
  }

  isFavorite(id: number): boolean {
    const favorites = JSON.parse(localStorage.getItem('favorites') || '[]');
    return favorites.find((p: any) => p.id === id);
  }

  onHoverIcon(event: Event, index: number) {
    const iconElement = event.target as HTMLElement;
    this.renderer.setStyle(iconElement, 'transition', 'transform 0.3s ease');
    this.renderer.setStyle(iconElement, 'transform', 'scale(1.2)');
    this.iconNames[index] = 'star-half-outline';
  }

  onLeaveIcon(event: Event, index: number) {
    const iconElement = event.target as HTMLElement;
    this.renderer.setStyle(iconElement, 'transition', 'transform 0.3s ease');
    this.renderer.setStyle(iconElement, 'transform', 'scale(1)');
    this.iconNames[index] = this.isFavorite(this.personajesList[index].id) ? 'star' : 'star-outline';
  }

  viewPersonaje(personaje: any) {
    this.personaje = personaje;
    this.isModalOpen = true;  // Abre el modal
  }

  closeModal() {
    this.isModalOpen = false;  // Cierra el modal
  }

  toggleFavorite(personaje: any, index: number) {
    let favorites = JSON.parse(localStorage.getItem('favorites') || '[]');
    if (favorites.find((p: any) => p.id === personaje.id)) {
      favorites = favorites.filter((p: any) => p.id !== personaje.id);
      this.iconNames[index] = 'star-outline';
    } else {
      favorites.push(personaje);
      this.iconNames[index] = 'star';
    }
    this._favoritesService.updateFavorites(favorites);  // Actualiza el servicio
  }
}
