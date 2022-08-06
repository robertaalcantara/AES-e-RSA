import socket
import time 
import sys

#TAMANHO MAXIMO QUE PODE SER ENCRIPTADO POR VEZ = 86 BYTES

def TCP_client(HEADER_SIZE):
    s = socket.socket()         
    host = "123.123.123.123"    
    port = 55443               
    f = open('arquivo.txt','rb')
    contador_pacotes = 0

    t0 = time.time()
    s.connect((host, port))

    end_of_file = False

    print("STARTED")

    while (not end_of_file):
        l = f.read(1000-HEADER_SIZE)   
        s.send(l)
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
