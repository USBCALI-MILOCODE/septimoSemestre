import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LocationServiceService {

  apiUrl = 'https://rickandmortyapi.com/api/location';

  constructor() { }

  getAllLocations() {
    return fetch(this.apiUrl)
      .then(response => response.json())
      .then(data => data.results)
  }
}
