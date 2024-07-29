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
VALUES ('Alexis', 'Sánchez', 'asanchez@gmail.com', '123456789', '123', 1);

INSERT INTO usuarios (nombre, apellido, correo, telefono, contrasena, rol_id)
VALUES ('Lenin', 'Llano', 'lllano@gmail.com', '987654321', '456', 2);


-- Crear la tabla hoteles
CREATE TABLE IF NOT EXISTS hotels (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    address VARCHAR(300)  NOT NULL,
    city VARCHAR(500)  NOT NULL
);

INSERT INTO hotels(
	 name, address, city)
VALUES ( 'Hotel Finlandia', 'Hotel en La Carolina, Quito', 'El Hotel Finlandia se encuentra en el distrito financiero, presenta unas instalaciones modernas y una decoración cálida y ofrece habitaciones con conexión Wi-Fi gratuita y TV de plasma.');

INSERT INTO hotels(
	 name, address, city)
VALUES ( 'Hotel Stubel Suites & Cafe', 'Hotel en La Floresta, Quito', 'El Hotel Stubel Suites es un alojamiento moderno situado en Quito que ofrece vistas impresionantes al valle del Guápulo.');

INSERT INTO hotels(
	 name, address, city)
VALUES ( 'Hotel Bellavista Quito', 'Hotel en Bellavista, Quito', 'El Hotel Bellavista Quito ofrece alojamiento con WiFi gratuita en Quito, en una zona comercial, a 5 minutos del parque La Carolina. Alberga un restaurante y un jardín.');

INSERT INTO hotels(
	 name, address, city)
VALUES ( 'NH Collection Quito Royal', 'Hotel en La Floresta, Quito', 'Este hotel se encuentra a 3 km del centro histórico de Quito, junto al World Trade Center, y ofrece alojamientos lujosos, centro de bienestar, WiFi gratuita y desayuno gratuito a partir de las 02:30...');

INSERT INTO hotels(
	 name, address, city)
VALUES ('Swissotel Quito', 'Hotel en La Floresta, Quito', 'El Swissôtel ofrece un alojamiento elegante en el sofisticado distrito comercial y residencial de Quito.');

INSERT INTO hotels(
	 name, address, city)
VALUES ( 'Hotel Savoy Inn', 'Hotel en Quito', 'El Hotel Savoy Inn, situado en los Andes, a solo unos minutos del famoso TelefériQo y del aeropuerto, ofrece habitaciones confortables con baño privado y magníficas vistas a la ciudad y a las montañas...');
