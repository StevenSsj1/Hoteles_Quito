import { Component } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { MatIconModule } from '@angular/material/icon';
import { FormControl, Validators, FormsModule, ReactiveFormsModule, FormGroup, FormBuilder } from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatDividerModule } from '@angular/material/divider';
import { HttpHeaders, HttpParams, HttpClient } from '@angular/common/http';
import { MatButtonModule } from '@angular/material/button';
import { merge } from 'rxjs';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [MatFormFieldModule, MatInputModule, FormsModule, ReactiveFormsModule, MatButtonModule, MatDividerModule, MatIconModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  email = new FormControl('', [Validators.required, Validators.email]);
  hide = true;
  errorMessage = '';
  mail: string = '';
  psw: string = '';
  form: FormGroup;
  token: string | null = null;

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

  constructor(
    private fb: FormBuilder,
    readonly http: HttpClient,
    private router: Router // Inyectar Router
  ) {
    merge(this.email.statusChanges, this.email.valueChanges)
      .pipe(takeUntilDestroyed())
      .subscribe(() => this.updateErrorMessage());
    this.form = this.fb.group({
      mail: ['', Validators.required],
      psw: ['', Validators.required]
    });
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

  login() {
    this.mail = this.form.get('mail')?.value;
    this.psw = this.form.get('psw')?.value;
    const body = new HttpParams()
      .set('username', this.mail)
      .set('password', this.psw);

    this.http.post('http://localhost:8000/api/token', body.toString(), {
      headers: new HttpHeaders().set('Content-Type', 'application/x-www-form-urlencoded')
    }).subscribe(responseData => {
      if (typeof responseData === 'object' && 'access_token' in responseData) {
        this.token = (responseData as { access_token: string }).access_token;
        this.datos();
      } else {
        console.error('No se encontró el token de acceso en la respuesta');
      }
    });

    this.router.navigate(['/home']).then(() => {
      this.updateButtonVisibility();
    });
  }

  datos() {
    const token = this.token;
    const url = 'http://localhost:8000/api/users/me';

    fetch(url, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then(data => {
      localStorage.setItem('rol_id', data.rol_id.toString());
      localStorage.setItem('correo', data.correo);
      // Redirigir a la ruta home después de guardar los datos
      this.router.navigate(['/home']);
    })
    .catch(error => console.error('Hubo un problema con la solicitud fetch:', error));
  }
}
