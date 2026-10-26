-- Ejecutar como administrador de MySQL (root). Cambia la contraseña de prueba.
CREATE DATABASE IF NOT EXISTS festival_votos
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'festival_user'@'localhost' IDENTIFIED BY 'cambia_esta_clave';
GRANT ALL PRIVILEGES ON festival_votos.* TO 'festival_user'@'localhost';
FLUSH PRIVILEGES;
