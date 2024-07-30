import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Observable } from 'rxjs';
import { MatTableModule } from '@angular/material/table';

interface Hotel {
  name: string;
  address: string;
  city: string;
  id: number;
}

@Component({
  selector: 'app-hotel-list',
  templateUrl: './hotel-list.component.html',
  styleUrls: ['./hotel-list.component.css'],
  standalone: true,
  imports: [MatTableModule, HttpClientModule]
})
export class HotelListComponent implements OnInit {
  displayedColumns: string[] = ['name', 'address', 'city'];
  dataSource: Hotel[] = [];

  private apiUrl = 'http://localhost:8000/api/v1/hotels/';

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.getHotels().subscribe((data: Hotel[]) => {
      this.dataSource = data;
    });
  }

  getHotels(): Observable<Hotel[]> {
    return this.http.get<Hotel[]>(this.apiUrl);
  }
}
