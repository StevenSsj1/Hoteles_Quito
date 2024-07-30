import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { UserRegisterComponent } from './user-register/user-register.component';
import { HotelRegisterComponent } from './hotel-register/hotel-register.component';
import { HomeComponent } from './home/home.component';
import { HotelListComponent } from './hotel-list/hotel-list.component';
import { UserListComponent } from './user-list/user-list.component';

export const routes: Routes = [
    { path: 'home', component: HomeComponent },
    { path: 'hotel-register', component: HotelRegisterComponent },
    { path: 'login', component: LoginComponent },
    { path: 'user-register', component: UserRegisterComponent },
    { path: 'hotel-list', component: HotelListComponent },
    { path: 'user-list', component: UserListComponent },
    { path: '', redirectTo: '/home', pathMatch: 'full' },
    { path: '**', redirectTo: '/home', pathMatch: 'full' }
];