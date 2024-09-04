import { Component, OnInit } from '@angular/core';
import { LocationServiceService } from 'src/app/services/location-service.service';
import { RickyMortyServiceService } from 'src/app/services/ricky-morty-service.service';

@Component({
  selector: 'app-lugares',
  templateUrl: './lugares.component.html',
  styleUrls: ['./lugares.component.scss'],
})
export class LugaresComponent implements OnInit {

  lugaresList: any = [];
  residentesList: { [key: string]: any[] } = {};
  loading: boolean = true; // Estado de carga

  constructor(
    private _locationService: LocationServiceService,
    private _rickyMortyService: RickyMortyServiceService
  ) { }

  ngOnInit() {
    this.getAllLocations();
  }

  getAllLocations() {
    this._locationService.getAllLocations()
      .then(data => {
        this.lugaresList = data;
        this.lugaresList.forEach((lugar: any) => {
          this.obtenerResidentes(lugar);
        });
        this.loading = false; // Termina la carga cuando los lugares están listos
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
}
