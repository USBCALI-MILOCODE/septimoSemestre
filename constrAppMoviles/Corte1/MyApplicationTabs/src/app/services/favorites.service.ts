import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FavoritesService {

  private favoriteSubject = new BehaviorSubject<any[]>(JSON.parse(localStorage.getItem('favorites') || '[]'));
  favorites$ = this.favoriteSubject.asObservable();

  updateFavorites(favorites: any[]) {
    this.favoriteSubject.next(favorites);
    localStorage.setItem('favorites', JSON.stringify(favorites));
  }
}
