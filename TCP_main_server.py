from TCP_server import TCP_server_AES, TCP_server_RSA
import time

HEADER_SIZE = 54

for i in range(12):
    TCP_server_AES(HEADER_SIZE, (i==11))
    print(f"Finished iteration {i}")
    time.sleep(0.1)
