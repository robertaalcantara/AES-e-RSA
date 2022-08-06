import socket
import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes

HOST = "123.123.123.123"  
PORT = 55443  

def TCP_server_RSA():
    f = open('arquivo_recebido.txt', 'wb')

    #generate the RSA key
    rsa_key = RSA.generate(1024)
    rsa_private_key = rsa_key.export_key()
    
    rsa_public_key = rsa_key.publickey().export_key()

    file_out = open("public_key.pem", "wb")
    file_out.write(rsa_public_key)
    file_out.close()

    file_out = open("private.pem", "wb")
    file_out.write(rsa_private_key)
    file_out.close()

    private_key = RSA.import_key(open("private.pem").read())
    chiper_rsa = PKCS1_OAEP.new(private_key)
    
    print("READY")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        
        conn, addr = s.accept()

        file_out = open("public_key.pem", "rb")
        l = file_out.read(271)
        conn.send(l)
        file_out.close()

        encrypted_l = conn.recv(1024)

        while(encrypted_l):
            for i in range(8):
                chunk = encrypted_l[128*i:128*(i+1)]
                if i==0:
                    l = chiper_rsa.decrypt(chunk)
                else:
                    l += chiper_rsa.decrypt(chunk)
            f.write(l)
            encrypted_l = conn.recv(1024)
        
        print("saiu while")
        conn.close()
        f.close()
        

def TCP_server_AES(HEADER_SIZE):
    f = open('arquivo_recebido.txt', 'wb')
    key = get_random_bytes(16)

    print("READY")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        
        conn, addr = s.accept()

        conn.send(key)

        encrypted_l = conn.recv(1000-HEADER_SIZE)
        nonce = encrypted_l[:16]
        tag = encrypted_l[16:32]
        chunk = encrypted_l[32:]
        ciphertext = chunk
        cipher = AES.new(key, AES.MODE_EAX, nonce)

        while(chunk):
            chunk = conn.recv(1000-HEADER_SIZE)
            ciphertext += chunk
        
        print("ACABOU WHILE")
        conn.close()

        print("DECRIPTANDO...")
        t0=time.time()
        l = cipher.decrypt_and_verify(ciphertext, tag)
        f.write(l)
        t1=time.time()
        print(f"tempo: {t1-t0}")
        f.close()
        print("ACABOU TD")
        

def TCP_server(HEADER_SIZE):
    f = open('arquivo_recebido.txt', 'wb')

    print("READY")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        
        conn, addr = s.accept()

        l=conn.recv(1000-HEADER_SIZE)
        while(l):
            l = conn.recv(1000-HEADER_SIZE)
            f.write(l)
        
        print("ACABOU WHILE")
        conn.close()

        f.close()