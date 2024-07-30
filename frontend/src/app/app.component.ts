import { Component, OnInit } from '@angular/core';
import { RouterLink, RouterLinkActive,RouterOutlet } from '@angular/router';
import { UserRegisterComponent } from './user-register/user-register.component';
import { HttpClientModule } from '@angular/common/http';
import { LoginComponent } from './login/login.component';
import { HotelRegisterComponent } from './hotel-register/hotel-register.component';
import { HomeComponent } from './home/home.component';
import { HotelListComponent } from './hotel-list/hotel-list.component';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, UserRegisterComponent, LoginComponent,HttpClientModule,HotelRegisterComponent,HomeComponent,HotelListComponent,RouterLink,RouterLinkActive,CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})

export class AppComponent implements OnInit {

  constructor(private router: Router) {}

  title = 'frontend';
  showLoginButton: boolean = true;
  showRegisterButton: boolean = true;
  routes: any;

  ngOnInit() {
    const rolId = localStorage.getItem('rol_id');
    const correo = localStorage.getItem('correo');

    if (rolId && correo) {
      this.showLoginButton = false;
      this.showRegisterButton = false;
    }
  }

  updateButtonVisibility() {
    const rolId = localStorage.getItem('rol_id');
    const correo = localStorage.getItem('correo');

    // Si rolId y correo están presentes, no mostrar los botones de inicio de sesión y registro
    if (rolId && correo) {
      this.showLoginButton = false;
      this.showRegisterButton = false;
    } else {
      this.showLoginButton = true;
      this.showRegisterButton = true;
    }
  }

  logout() {
    // Borrar datos del local storage
    localStorage.removeItem('rol_id');
    localStorage.removeItem('correo');
    
    // Redirigir al usuario a la ruta de home y actualizar la visibilidad de los botones
    this.router.navigate(['/home']).then(() => {
      // Actualizar la visibilidad de los botones después de la redirección
      this.updateButtonVisibility();
    });
  }
}