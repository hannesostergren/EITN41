from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from base64 import b64decode

def construct_key(key):
    secret_key = RSA.importKey(open(key, 'rb').read())
    e, p, q, d = [getattr(secret_key, s) for s in ['e', 'p', 'q', 'd']]
    n = p * q
    return  RSA.construct((n, e, d, p, q))

def decrypt_message(msg, privet_key):
    decoded_data = b64decode(msg)
    sentinel = Random.new().read(15)
    cipher = PKCS1_v1_5.new(privet_key)
    message = cipher.decrypt(decoded_data, sentinel)
    return message.decode('utf8').strip()

def censored_RSA(msg, key):
    privet_key = construct_key(key)
    decrypted_msg = decrypt_message(msg, privet_key)
    return decrypted_msg

def start():
    key = input('Chose a .pem key: ')
    msg = input('Secret message: ')
    decrypted_msg = censored_RSA(msg,key)
    print(decrypted_msg)

start()