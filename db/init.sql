-- Crear la base de datos si no existe
SELECT 'CREATE DATABASE dbname'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'dbname')\gexec

-- Conectar a la base de datos
\c dbname;

-- Crear la tabla roles
CREATE TABLE IF NOT EXISTS roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT
);

-- Insertar roles por defecto
INSERT INTO roles (name, description) VALUES ('admin', 'Administrator role');
INSERT INTO roles (name, description) VALUES ('user', 'User role');

-- Crear la tabla usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    correo VARCHAR(255) UNIQUE NOT NULL,
    telefono VARCHAR(255),
    contrasena VARCHAR(255) NOT NULL,
    rol_id INTEGER REFERENCES roles(id)
);

-- Insertar algunos usuarios de ejemplo
INSERT INTO usuarios (nombre, apellido, correo, telefono, contrasena, rol_id)
VALUES ('Juan', 'Perez', 'juan@example.com', '123456789', 'password', 1);

INSERT INTO usuarios (nombre, apellido, correo, telefono, contrasena, rol_id)
VALUES ('Maria', 'Gonzalez', 'maria@example.com', '987654321', 'securepassword', 2);
