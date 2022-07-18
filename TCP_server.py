import socket
import time
import pickle
from Crypto.PublicKey import RSA
from Crypto.Util import randpool

HOST = "123.123.123.123"  
PORT = 55443  

def TCP_server(HEADER_SIZE, extra_sleep):
    f = open('arquivo_recebido.txt', 'wb')

    #generate the RSA key
    blah = randpool.RandomPool()
    RSAKey = RSA.generate(512, blah.get_bytes)
    
    RSAPubKey = RSAKey.publickey()
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        
        conn, addr = s.accept()
        l = conn.recv(1000 - HEADER_SIZE)
        conn.send(pickle.dumps(RSAPubKey))

        rcstring = ''
        while 1:
            buf = conn.recv(1024)
            rcstring += buf
            if not len(buf):
                break

        """
        while(l):
            f.write(l)
            l = conn.recv(1000 - HEADER_SIZE)
        if extra_sleep:
            time.sleep(5)
        """
        f.close()
        conn.close()

        encmessage = pickle.loads(rcstring)
        print(encmessage)