import socket
import random
import hashlib

SOC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
SOC.connect(("eitn41.eit.lth.se", 1337))
p = int('FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF', 16)
g = 2
SHARED_SECRET = "eitn41 <3"

def receive():
    message = SOC.recv(4096).decode('utf8').strip()
    return message

def send(message):
    formatted_message = format(message, 'x')
    SOC.send(formatted_message.encode('utf8'))

def gen_g(g):
    r = random.randint(1, p)
    ret = pow(g, r, p)
    return ret, r

def xor(a, b):
    return bytes(i ^j for i, j in zip(bytes.fromhex(a), bytes.fromhex(b)))

def main():

    ##########################
    #### D-H Key Exchange ####
    ##########################

    g_x1 = int(receive(), 16)
    g_x2, x2 = gen_g(g)
    send(g_x2)
    print('\nsent g_x2:', receive())

    ###############################
    #### Socialist Millionaire ####
    ###############################

    g_a2 = int(receive(), 16)
    g_b2, b2 = gen_g(g)
    send(g_b2)
    print("sent g_b2: ", receive())

    g_a3 = int(receive(), 16)
    g_b3, b3 = gen_g(g)
    send(g_b3)
    print("sent g_b3: ", receive())

    P_a = int(receive(), 16)
    g3 = pow(g_a3, b3, p)
    P_b, b = gen_g(g3)

    send(P_b)
    print("sent P_b: ", receive())

    Q_a = int(receive(), 16)
    g2 = pow(g_a2, b2, p)
    g_x1x2 = pow(g_x1, x2, p)
    bytes_g_x1x2 = g_x1x2.to_bytes((g_x1x2.bit_length() + 7) // 8, 'big')
    y = hashlib.sha1(bytes_g_x1x2 + SHARED_SECRET.encode('utf-8')).hexdigest()
    y = int(y, 16)
    Q_b = pow(g, b, p) * pow(g2, y, p)
    send(Q_b)
    print("sent Q_b: ", receive())

    R_a = int(receive(), 16)
    R_b = pow(Q_a * pow(Q_b, -1, p), b3, p)
    send(R_b)
    print("sent R_b: ", receive())
    print("Auth: ", receive())

    
    #####################
    #### Secure Chat ####
    #####################

    print("Secure chat:")
    message = "427541422c9f68f2b4ea663b07f0da19d51b4b53"
    hex_mess = int(message, 16)
    send(hex_mess ^ g_x1x2)
    print("response: ", receive())



if __name__ == "__main__":
    main()