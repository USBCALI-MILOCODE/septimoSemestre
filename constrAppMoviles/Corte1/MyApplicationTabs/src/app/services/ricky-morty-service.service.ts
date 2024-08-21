import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class RickyMortyServiceService {

  apiURL = 'https://rickandmortyapi.com/api/character/';

  constructor() { }

  getAllCharacters() {
    return fetch(this.apiURL)
      .then(response => response.json())
      .then(data => data.results)
  }

  getCharacterById(id: string | null) {
    return fetch(`${this.apiURL}${id}`)
      .then(response => response.json())
      .then(data => data)
  }

  getCharacterByUrl(url: string) {
    return fetch(url)
      .then(response => response.json())
      .then(data => data);
  }
}
