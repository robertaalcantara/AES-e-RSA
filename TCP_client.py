import socket
import time 
import sys
from Crypto.PublicKey import RSA
import pickle

def TCP_client(HEADER_SIZE):
    s = socket.socket()         
    host = "123.123.123.123"    
    port = 55443               
    f = open('pokemon.txt','rb')
    contador_pacotes = 0

    t0 = time.time()
    s.connect((host, port))
    l = f.read(1000-HEADER_SIZE)

    #this should loop around until a delimeter is read
    #or something similar
    rcstring = s.recv(2048)
    
    #this object is of type RSAobj_c, which only has public key
    #encryption is possible, but not decryption
    publickey = pickle.loads(rcstring)
    
    print(publickey)
    
    #encrypt the top secret data
    secretText = publickey.encrypt("Hello, this is Rich.", 32)
    
    s.sendall(pickle.dumps(secretText))

    """
    while (l):
        s.send(l)
        contador_pacotes+=1
        time.sleep(sys.float_info.min)
        l = f.read(1000-HEADER_SIZE)
    """
    s.shutdown(socket.SHUT_WR)
    s.close()
    t1 = time.time()
    f.close()

    return t1-t0, contador_pacotes