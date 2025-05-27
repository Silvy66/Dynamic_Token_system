# Dynamic_Token_system
Este proyecto simula una transacción segura entre dos contenedores Docker que se comunican usando sockets TCP, incorporando un sistema de **clave dinámica** tipo OTP (One-Time Password) con **HMAC + SHA256**,  para validar operaciones.

🧩 Componentes Principales<br>
Componente<br>
Descripción:
Cliente (cliente.py): Simula una aplicación cliente que inicia una transacción con un token dinámico.<br>
Servidor (server.py): Recibe la transacción y verifica la validez del token antes de aceptarla o rechazarla.<br>
Shared/config.py : Contiene funciones para generar y verificar tokens seguros. Docker Compose : Orquesta el entorno completo, creando la red y lanzando los servicios en contenedores.<br>
Docker Hub: Fuente de imágenes preconstruidas del cliente y servidor (silvy6/cliente_dockerfile, silvy6/servidor_dockerfile).<br>
GitHub: Repositorio principal donde vive el código fuente y el archivo docker-compose.yml.<br>


## Resumen del Flujo <br>
- El desarrollador clona el proyecto desde GitHub.
- Ejecuta docker compose up sin build
- Docker Compose orquesta la red y los servicios.
- Docker Compose descarga las imágenes cliente y servidor desde DockerHub.
- Los contenedores cliente y servidor usan imágenes descargadas desde DockerHub.
- Cliente genera un token con HMAC + SHA256 usando una clave secreta compartida y lo envía junto con una transacción al servidor.
- Servidor valida el token y responde.
- Ambos se comunican mediante sockets TCP dentro de una red Docker bridge.
- El sistema usa código compartido (shared/config.py) para generar y validar tokens dinámicos.

## ¿Cómo Ejecuto el Poryecto? 


