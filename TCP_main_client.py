from TCP_client_AES import TCP_client_AES
from TCP_client_RSA import TCP_client_RSA 
from TCP_client import TCP_client 
import time
import pandas as pd
from os.path import exists

HEADER_SIZE = 66

tempos = []
total_pacotes = []

for i in range(11):
    tempo, contador_pacotes = TCP_client(HEADER_SIZE)

    print(f"Finished iteration {i} {tempo} seg")
    results = pd.DataFrame({
            'Tempos': [tempo],
            'Pacotes': [contador_pacotes]
        })

    if not exists("ResultadosRSA.csv"):
        results.to_csv("ResultadosRSA.csv",index=False)
    else:
        file_df = pd.read_csv("ResultadosRSA.csv")
        file_df = pd.concat([file_df,results], ignore_index=True)
        file_df.to_csv("ResultadosRSA.csv",index=False)
    
    time.sleep(180)
time.sleep(1)
