import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { UserRegisterComponent } from './user-register/user-register.component';
import { HttpClientModule } from '@angular/common/http';
import { LoginComponent } from './login/login.component';
import { HotelRegisterComponent } from './hotel-register/hotel-register.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, UserRegisterComponent, LoginComponent,HttpClientModule,HotelRegisterComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'frontend';
}
