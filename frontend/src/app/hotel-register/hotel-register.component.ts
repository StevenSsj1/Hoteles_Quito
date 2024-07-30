import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-hotel-register',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './hotel-register.component.html',
  styleUrls: ['./hotel-register.component.css']
})
export class HotelRegisterComponent {
  form: FormGroup;
  name: string = '';
  address: string = '';
  city: string = '';
  description: string = '';

  constructor(private fb: FormBuilder,private router: Router ) {
    this.form = this.fb.group({
      name: ['', Validators.required],
      address: ['', Validators.required],
      city: ['', Validators.required],
      description: ['', Validators.required]
    });
  }

  guardar() {
    this.name = this.form.get('name')?.value;
    this.address = this.form.get('address')?.value;
    this.city = this.form.get('city')?.value;
    this.description = this.form.get('description')?.value;
  }

  crear_hotel() {
    this.guardar();
    fetch('http://localhost:8000/api/v1/hotels/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        name: this.name,
        address: this.address,
        city: this.city,
      })
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
    alert('Hotel registrado');
    this.router.navigate(['/home']);
  }

  
}
