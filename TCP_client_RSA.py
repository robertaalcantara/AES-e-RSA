import socket
import time 
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def TCP_client_RSA(HEADER_SIZE):
    s = socket.socket()         
    host = "123.123.123.123"    
    port = 55443               
    f = open('arquivo.txt','rb')
    contador_pacotes = 0

    t0 = time.time()
    s.connect((host, port))

    rcstring = s.recv(271)
    key = RSA.import_key(rcstring)
    cipher_rsa = PKCS1_OAEP.new(key)

    end_of_file = False

    print("STARTED")

    while (not end_of_file):
        for i in range(8): 
            l = f.read(86)   
            if i == 0:
                encrypted_l = cipher_rsa.encrypt(l)
            else:
                encrypted_l += cipher_rsa.encrypt(l)
        s.send(encrypted_l)
        contador_pacotes+=1
        time.sleep(sys.float_info.min)
        if not l:
            end_of_file = True
        
    s.shutdown(socket.SHUT_WR)
    s.close()
    t1 = time.time()
    print(t1-t0)
    f.close()

    return t1-t0, contador_pacotes

if __name__ == '__main__':
    TCP_client_RSA(66)