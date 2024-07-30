import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-user-register',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './user-register.component.html',
  styleUrl: './user-register.component.css'
})
export class UserRegisterComponent {

  form: FormGroup;
  nombre: string ='';
  apellido: string='';
  email: string='';
  telefono: string='';
  password: string='';
  rol: number=0;
  
  guardar(){
    this.nombre=this.form.get('nombre')?.value
    this.apellido=this.form.get('apellido')?.value
    this.email=this.form.get('correo')?.value
    this.telefono=this.form.get('telefono')?.value
    this.password=this.form.get('contrasena')?.value
    this.rol=this.form.get('opciones')?.value
  }

  constructor(private fb:FormBuilder,private router: Router){
    this.form=this.fb.group({
        nombre:['',Validators.required],
        apellido:['',Validators.required],
        correo:['',Validators.required],
        telefono:['',Validators.required],
        contrasena:['',Validators.required],
        opciones:['',Validators.required]
    })
  }

  crear_usuario(){
    this.guardar()
    fetch('http://localhost:8000/api/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(
        {
          nombre: this.nombre,
          apellido: this.apellido,
          correo: this.email,
          telefono: this.telefono,
          contrasena: this.password,
          rol_id: this.rol
        }
      )
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error))
    alert('Usuario registrado');
    this.router.navigate(['/home']);
  }
}


