import socket
import json
from shared.config import verificar_token

HOST = ''
PORT = 5000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Servidor esperando conexión...")
        
        conn, addr = s.accept()
        with conn:
            print(f"Conexión establecida desde {addr}")
            data = conn.recv(1024).decode()
            transaccion = json.loads(data)

            if verificar_token(transaccion.get("token")):
                respuesta = "Transacción aceptada"
            else:
                respuesta = "Token inválido"

            print(f"Transacción recibida: {transaccion}")
            conn.sendall(respuesta.encode())

if __name__ == "__main__":
    main()
