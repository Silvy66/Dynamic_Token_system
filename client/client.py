import socket
import json
from shared.config import generar_token

HOST = 'server'  # nombre del contenedor del servidor en docker-compose
PORT = 5000

def main():
    transaccion = {
        "de": "cliente_001",
        "para": "comercio_abc",
        "monto": 10000,
        "token": generar_token()
    }
    print("[CLIENTE] Iniciando conexión con el servidor...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("[CLIENTE] Enviando transacción:", transaccion)
        s.sendall(json.dumps(transaccion).encode())
        respuesta = s.recv(1024).decode()
        print(f"Respuesta del servidor: {respuesta}")

if __name__ == "__main__":
    main()
