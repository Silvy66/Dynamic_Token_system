# 🔐 Sistema de Transacciones con Clave Dinámica (Tipo Bancolombia) usando Docker y Python

Este proyecto simula una transacción segura entre dos contenedores Docker que se comunican usando sockets TCP, incorporando un sistema de **clave dinámica** tipo OTP (One-Time Password) con **HMAC + SHA256**, similar al empleado por Bancolombia para validar operaciones.

---

## 📦 Tabla de Contenidos

- [🧩 Descripción](#🧩-descripción)
- [🛠️ Requisitos](#🛠️-requisitos)
- [📁 Estructura del Proyecto](#📁-estructura-del-proyecto)
- [🔐 Lógica Criptográfica](#🔐-lógica-criptográfica)
- [🚀 Cómo Ejecutarlo](#🚀-cómo-ejecutarlo)
- [🔁 Flujo de una Transacción](#🔁-flujo-de-una-transacción)
- [🧪 Ejemplo de Transacción](#🧪-ejemplo-de-transacción)
- [👨‍💻 Autores](#👨‍💻-autores)

---

## 🧩 Descripción

Este sistema distribuye su funcionamiento en **dos servicios**:

- **Cliente:** Envía una transacción junto con un token OTP válido.
- **Servidor:** Verifica el token y aprueba o rechaza la transacción.

La comunicación se realiza mediante sockets TCP entre contenedores Docker, sin necesidad de interfaz gráfica.

---

## 🛠️ Requisitos

Asegúrate de tener lo siguiente instalado en tu máquina:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python 3.11+](https://www.python.org/)
- [Visual Studio Code (opcional)](https://code.visualstudio.com/)
- Git (para clonar el repositorio)

---

## 📁 Estructura del Proyecto


dynamic_token_system/
├── client/
│   ├── Dockerfile
│   └── client.py
├── server/
│   ├── Dockerfile
│   └── server.py
├── shared/
│   └── config.py        # Lógica compartida para tokens
├── docker-compose.yml   # Orquestación de servicios
└── README.md             # Documentación del proyecto

🔐 Lógica Criptográfica
El sistema utiliza HMAC (Hash-based Message Authentication Code) con el algoritmo SHA256 para generar claves dinámicas cada 30 segundos (Time-based OTP). Tanto el cliente como el servidor comparten una clave secreta que no se transmite.

Token Dinámico
El token se calcula como:


HMAC_SHA256(secret_key, timestamp // 30)
Esto genera un token único por cada bloque de 30 segundos.

🚀 Cómo Ejecutarlo
1. Clona el repositorio

git clone https://github.com/tuusuario/dynamic_token_system.git
cd dynamic_token_system
2. Ejecuta los servicios con Docker


docker-compose up --build
Esto levantará los dos contenedores:

El servidor escucha en el puerto 5000.

El cliente se conecta y envía una transacción con token dinámico.

Verás la respuesta del servidor directamente en la terminal del cliente.

🔁 Flujo de una Transacción
El cliente genera un token dinámico válido (válido por 30 segundos).

El cliente arma una transacción con:

ID emisor

ID receptor

Monto

Token

El servidor recibe la transacción.

Verifica el token usando la misma clave secreta compartida.

Responde con:

✅ "Transacción aceptada" si el token es válido.

❌ "Token inválido" si no lo es.

🧪 Ejemplo de Transacción
Ejemplo JSON transmitido:


{
  "de": "cliente_001",
  "para": "comercio_abc",
  "monto": 10000,
  "token": "9c8f1e5f46bdf15dd894..."
}
🔐 Seguridad
El sistema no transmite la clave secreta.

Los tokens expiran cada 30 segundos.

Se permite una pequeña tolerancia de tiempo para evitar rechazos por latencia de red.

La comunicación entre contenedores es local, pero puedes agregar TLS o VPN en producción.

GitHub: @Silvy66