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
- Ambos usan código compartido (shared/config.py) para generar y validar tokens dinámicos.
- Servidor valida el token y responde.
- Ambos se comunican mediante sockets TCP dentro de una red Docker bridge.
### Estructura del proyecto
![image](https://github.com/user-attachments/assets/4ed134fb-37e4-4c96-884f-bd8ebc1b5582)

## ¿Cómo Ejecuto el Proyecto? 
## 🛠️ Requisitos

Asegúrate de tener lo siguiente instalado en tu máquina:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python 3.11+](https://www.python.org/)
- [Visual Studio Code (opcional)](https://code.visualstudio.com/)
- GitHub (para clonar el repositorio)

## Ejecución

-  Clona el repositorio
[Repositorio ](https://github.com/Silvy66/Dynamic_Token_system.git)
-  Ejecuta los servicios con Docker. El docker-compose.yml usa imágenes ya publicadas en Docker Hub:

[Servidor: servidor_dockerfile](https://hub.docker.com/repository/docker/silvy6/servidor_dockerfile/general)

[Cliente: cliente_dockerfile](https://hub.docker.com/repository/docker/silvy6/cliente_dockerfile/general)

- ➡️ Esto significa que las imágenes ya están preconstruidas y se descargan automáticamente desde el repositorio de Docker Hub, ejecutando en la terminal de tu IDE, el siguiente comando:

## "docker compose up"

- ➡️ En ese momento, Docker:

Descarga las imágenes del servidor y cliente.
Crea los contenedores basados en esas imágenes.
Los conecta a una red interna (secure_net) tipo bridge.
Verás la respuesta del servidor directamente en la terminal del cliente.
 
![image](https://github.com/user-attachments/assets/66527cd0-0ad4-4fd1-a2f8-0d191c2225d7)

## Arquitectura del Sistema
![image](https://github.com/user-attachments/assets/45598887-6cb3-40bb-a4ac-1f07a8596a36)

## ✅ Ventajas de esta Arquitectura
### Ventaja
### Descripción: <br>
Portabilidad: El sistema se puede ejecutar en cualquier máquina con Docker instalado. Escalabilidad: Se pueden lanzar múltiples instancias del cliente para simular carga. Aislamiento: Cada componente corre en su propio contenedor. Seguridad Extendible: Es posible integrar TLS, JWT o firmas digitales. Automatización futura (CI/CD): Puedes conectar GitHub con DockerHub para actualizar imágenes automáticamente.

📊 Posible Mejora Reemplazar la conexión con sockets por un API REST (Flask, FastAPI).

Agregar persistencia (base de datos) para registrar transacciones.

Implementar rotación de claves dinámicas cada X minutos. <br>
GitHub: @Silvy66
