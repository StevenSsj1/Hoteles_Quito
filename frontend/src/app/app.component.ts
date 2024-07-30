import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive,RouterOutlet } from '@angular/router';
import { UserRegisterComponent } from './user-register/user-register.component';
import { HttpClientModule } from '@angular/common/http';
import { LoginComponent } from './login/login.component';
import { HotelRegisterComponent } from './hotel-register/hotel-register.component';
import { HomeComponent } from './home/home.component';
import { HotelListComponent } from './hotel-list/hotel-list.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, UserRegisterComponent, LoginComponent,HttpClientModule,HotelRegisterComponent,HomeComponent,HotelListComponent,RouterLink,RouterLinkActive],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'frontend';
}
