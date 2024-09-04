import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { RickyMortyServiceService } from 'src/app/services/ricky-morty-service.service';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss'],
})
export class SearchComponent implements OnInit {
  personajes: any[] = [];
  personajesFiltrados: any[] = [];
  searchQuery: string = ''; // Variable para almacenar la consulta de búsqueda

  constructor(private rickyMortyService: RickyMortyServiceService) {
    this.loadAllCharacters();
  }

  ngOnInit(): void {
    // No es necesario lanzar un error aquí
  }

  // Método para cargar todos los personajes desde todas las páginas de la API
  async loadAllCharacters() {
    let page = 1;
    let morePagesAvailable = true;

    while (morePagesAvailable) {
      try {
        const characters = await this.rickyMortyService.getAllCharacters(page);
        this.personajes.push(...characters);

        // Verificar si la página actual tiene personajes, de lo contrario, detener la carga
        morePagesAvailable = characters.length > 0;
        page++;
      } catch (error) {
        console.error('Error fetching characters:', error);
        morePagesAvailable = false; // Detener la carga si hay un error
      }
    }

    this.personajesFiltrados = []; // Lista vacía inicialmente
  }

  // Método para filtrar personajes según la entrada de búsqueda
  onSearch(event: any) {
    this.searchQuery = event.target.value; // Actualizar la consulta de búsqueda
    const query = this.searchQuery.toLowerCase();

    if (query.trim() === '') {
      this.personajesFiltrados = [];
    } else {
      this.personajesFiltrados = this.personajes.filter(personaje =>
        personaje.name.toLowerCase().includes(query)
      );
    }
  }

}
