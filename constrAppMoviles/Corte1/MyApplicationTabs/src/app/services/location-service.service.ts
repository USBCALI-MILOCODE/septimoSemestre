import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LocationServiceService {

  apiUrl = 'https://rickandmortyapi.com/api/location';

  constructor() { }

  getLocationsByPage(page: number) {
    return fetch(`${this.apiUrl}?page=${page}`)
      .then(response => response.json());
  }
}
