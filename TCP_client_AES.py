import socket
import time 
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from idna import check_hyphen_ok

#TAMANHO MAXIMO QUE PODE SER ENCRIPTADO POR VEZ = 86 BYTES

def TCP_client_AES(HEADER_SIZE):
    s = socket.socket()         
    host = "123.123.123.123"    
    port = 55443               
    f = open('pokemon.txt','rb')
    contador_pacotes = 0

    t0 = time.time()
    s.connect((host, port))

    key = s.recv(16)
    cipher = AES.new(key, AES.MODE_EAX)

    l = f.read()   
    ciphertext, tag = cipher.encrypt_and_digest(l)

    size_pacote = 1000-HEADER_SIZE
    
    #1000 - 16 do nonce e 16 da tag
    s.send(cipher.nonce+tag+ciphertext[:968-HEADER_SIZE])
    contador_pacotes+=1

    i = 968-HEADER_SIZE
    print("STARTED")
    while (i < len(ciphertext)):
        if contador_pacotes%10000==0:
            print(f"pacote: {contador_pacotes}")
        if i+size_pacote < len(ciphertext):
            chunk = ciphertext[i:i+size_pacote]
        else:
            chunk = ciphertext[i:]
        i += size_pacote
        s.send(chunk)
        contador_pacotes+=1
        time.sleep(sys.float_info.min)        
    t1 = time.time()
    time.sleep(1)
    print(f"{t1-t0} seg, {contador_pacotes} pacotes")
    f.close()

    s.shutdown(socket.SHUT_WR)
    s.close()
    return t1-t0, contador_pacotes

if __name__ == '__main__':
    TCP_client_AES(66)