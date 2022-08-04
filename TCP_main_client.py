from TCP_client_AES import TCP_client_AES
from TCP_client_RSA import TCP_client_RSA 
import time
import pandas as pd
from os.path import exists

HEADER_SIZE = 54

tempos = []
total_pacotes = []

for i in range(11):
    time.sleep(1)
    tempo, contador_pacotes = TCP_client_AES(HEADER_SIZE)
    #tempos.append(tempo)
    #total_pacotes.append(contador_pacotes)
    print(f"Finished iteration {i} {tempo} seg")
    results = pd.DataFrame({
            'Tempos': tempo,
            'Pacotes': contador_pacotes
        })

    if not exists("ResultadosAES.csv"):
        results.to_csv("ResultadosAES.csv",index=False)
    else:
        file_df = pd.read_csv("ResultadosAES.csv")
        file_df = pd.concat([file_df,results], ignore_index=True)
        file_df.to_csv("ResultadosAES.csv",index=False)
    
    time.sleep(2)
time.sleep(1)
