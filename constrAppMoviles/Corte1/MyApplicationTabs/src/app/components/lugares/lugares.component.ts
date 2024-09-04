import { Component, OnInit } from '@angular/core';
import { LocationServiceService } from 'src/app/services/location-service.service';
import { RickyMortyServiceService } from 'src/app/services/ricky-morty-service.service';

@Component({
  selector: 'app-lugares',
  templateUrl: './lugares.component.html',
  styleUrls: ['./lugares.component.scss'],
})
export class LugaresComponent implements OnInit {
  lugaresList: any[] = [];
  residentesList: { [key: string]: any[] } = {};
  loading: boolean = true;
  page: number = 1; // Página actual para la paginación
  hasMoreLocations: boolean = true; // Control para saber si hay más lugares para cargar

  constructor(
    private _locationService: LocationServiceService,
    private _rickyMortyService: RickyMortyServiceService
  ) { }

  ngOnInit() {
    this.getAllLocations();
  }

  getAllLocations() {
    this._locationService.getLocationsByPage(this.page)
      .then(data => {
        this.lugaresList = [...this.lugaresList, ...data.results];
        data.results.forEach((lugar: any) => {
          this.obtenerResidentes(lugar);
        });
        this.loading = false;
        this.hasMoreLocations = data.info.next !== null; // Verifica si hay más lugares
      });
  }

  obtenerResidentes(lugar: any) {
    const residents = lugar.residents;
    this.residentesList[lugar.id] = [];

    residents.forEach((url: string) => {
      this._rickyMortyService.getCharacterByUrl(url)
        .then(data => {
          this.residentesList[lugar.id].push(data);
        });
    });
  }

  loadMoreLocations(event: any) {
    if (this.hasMoreLocations) {
      this.page++;
      this.getAllLocations();
    }
    event.target.complete(); // Finaliza la animación de scroll infinito
  }
}
