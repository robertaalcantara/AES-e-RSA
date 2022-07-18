from TCP_server import TCP_server 
import time

HEADER_SIZE = 66

for i in range(12):
    TCP_server(HEADER_SIZE, (i==9))
    print(f"Finished iteration {i}")
    time.sleep(0.1)
