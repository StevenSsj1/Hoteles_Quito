import { Component } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { MatIconModule } from '@angular/material/icon';
import { FormControl, Validators, FormsModule, ReactiveFormsModule, FormGroup, FormBuilder } from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import {MatDividerModule} from '@angular/material/divider';
import { HttpHeaders, HttpParams,HttpClient , HttpClientModule } from '@angular/common/http';
import {MatButtonModule} from '@angular/material/button';
import { merge } from 'rxjs';

export interface Auth {
  access_token: string;
}
@Component({
  selector: 'app-login',
  standalone: true,
  imports: [MatFormFieldModule, MatInputModule, FormsModule, ReactiveFormsModule
    ,MatButtonModule, MatDividerModule, MatIconModule
  ],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  email = new FormControl('', [Validators.required, Validators.email]);
  hide = true;
  errorMessage = '';
  correo: string = '';
  psw: string = '';
  form: FormGroup;
  token: string | null=null;
  dataAuth: Auth | null=null;
  

  constructor(private fb: FormBuilder,readonly http: HttpClient) {
    merge(this.email.statusChanges, this.email.valueChanges)
      .pipe(takeUntilDestroyed())
      .subscribe(() => this.updateErrorMessage());
    this.form = this.fb.group({
      correo: ['', Validators.required],
      psw: ['', Validators.required]
    })
  }

  updateErrorMessage() {
    if (this.email.hasError('required')) {
      this.errorMessage = 'You must enter a value';
    } else if (this.email.hasError('email')) {
      this.errorMessage = 'Not a valid email';
    } else {
      this.errorMessage = '';
    }
  }
  
  login(username: 'prueba@gmail.com', password: '123') {
    const body = new HttpParams()
      .set('username', username)
      .set('password', password);
  
    this.http.post('http://localhost:8000/api/token',
      body.toString(),
      {
        headers: new HttpHeaders()
          .set('Content-Type', 'application/x-www-form-urlencoded')
      }
    ).subscribe(responseData => {
      console.log(responseData);
      if (typeof responseData === 'object' && 'access_token' in responseData) {
        this.token = (responseData as { access_token: string }).access_token;
        console.log('Token de acceso:', this.token);
      } else {
        console.error('No se encontró el token de acceso en la respuesta');
      }
      this.datos();
    });
    
  }

  datos() {
    // Supongamos que ya tienes el Bearer Token
    const token = this.token;

    // La URL a la que deseas hacer la petición
    const url = 'http://localhost:8000/api/users/me';

    // Realizar la petición fetch con el Bearer Token
    fetch(url, {
      method: 'GET', // O 'POST', 'PUT', 'DELETE', según sea necesario
      headers: {
        'Authorization': `Bearer ${token}`, // Incluir el Bearer Token en el encabezado
        'Content-Type': 'application/json' // Tipo de contenido, si es necesario
      }
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json(); // O response.text(), response.blob(), etc., según sea necesario
      })
      .then(data => {
        console.log('Datos recibidos:', data);
      })
      .catch(error => {
        console.error('Hubo un problema con la solicitud fetch:', error);
      });

  }
}



