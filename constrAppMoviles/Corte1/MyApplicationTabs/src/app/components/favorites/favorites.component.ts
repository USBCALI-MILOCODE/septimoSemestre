import { Component, OnInit } from '@angular/core';
import { FavoritesService } from 'src/app/services/favorites.service';

@Component({
  selector: 'app-favorites',
  templateUrl: './favorites.component.html',
  styleUrls: ['./favorites.component.scss'],
})
export class FavoritesComponent  implements OnInit {

  favorites: any[] = [];

  constructor(
    private _favoritesService: FavoritesService
  ) { }

  ngOnInit() {
    this._favoritesService.favorites$.subscribe(favorites => {
      this.favorites = favorites;
    });
  }

  removeFavorite(favorito: any) {
    const updatedFavorites = this.favorites.filter(f => f.id !== favorito.id);
    this._favoritesService.updateFavorites(updatedFavorites);
  }
}

