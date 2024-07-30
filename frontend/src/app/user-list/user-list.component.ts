import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Observable } from 'rxjs';
import { MatTableModule } from '@angular/material/table';
import { CommonModule } from '@angular/common';

interface User {
  nombre: string;
  apellido: string;
  correo: string;
  telefono: string;
  id: number;
  rol_id: number;
}

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.css'],
  standalone: true,
  imports: [CommonModule, MatTableModule, HttpClientModule]
})
export class UserListComponent implements OnInit {
  displayedColumns: string[] = ['nombre', 'apellido', 'correo', 'telefono', 'rol'];
  dataSource: User[] = [];

  private apiUrl = 'http://localhost:8000/api/users/';

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.getUsers().subscribe((data: User[]) => {
      this.dataSource = data.map(user => ({
        ...user,
        rol: this.getRole(user.rol_id)
      }));
    });
  }

  getUsers(): Observable<User[]> {
    return this.http.get<User[]>(this.apiUrl);
  }

  getRole(rol_id: number): string {
    return rol_id === 1 ? 'Administrador' : 'Cliente';
  }
}
