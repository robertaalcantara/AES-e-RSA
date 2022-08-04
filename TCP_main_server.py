from TCP_server import TCP_server_AES, TCP_server_RSA
import time

HEADER_SIZE = 54

for i in range(11):
    TCP_server_AES(HEADER_SIZE)
    print(f"Finished iteration {i}")
    time.sleep(0.1)
