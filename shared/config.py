import time
import hmac
import hashlib

SECRET_KEY = b'mi_clave_secreta_compartida'  # Debe ser compartida entre cliente y servidor

def generar_token(timestamp=None):
    if timestamp is None:
        timestamp = int(time.time() // 30)  # 30s de validez
    msg = str(timestamp).encode()
    return hmac.new(SECRET_KEY, msg, hashlib.sha256).hexdigest()

def verificar_token(token, margin=1):
    actual_timestamp = int(time.time() // 30)
    for i in range(-margin, margin + 1):  # Permitir margen de ±30s
        if hmac.new(SECRET_KEY, str(actual_timestamp + i).encode(), hashlib.sha256).hexdigest() == token:
            return True
    return False
