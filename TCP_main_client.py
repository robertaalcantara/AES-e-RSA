from TCP_client import TCP_client 
import time
import pandas as pd
from os.path import exists

HEADER_SIZE = 66

tempos = []
total_pacotes = []

for i in range(12):
    time.sleep(1)
    tempo, contador_pacotes = TCP_client(HEADER_SIZE)
    tempos.append(tempo)
    total_pacotes.append(contador_pacotes)
    print(f"Finished iteration {i} {tempo} seg")
time.sleep(1)

results = pd.DataFrame({
        'Tempos': tempos,
        'Pacotes': total_pacotes
    })

if not exists("Resultados.csv"):
    results.to_csv("Resultados.csv",index=False)
else:
    file_df = pd.read_csv("Resultados.csv")
    file_df = pd.concat([file_df,results], ignore_index=True)
    file_df.to_csv("Resultados.csv",index=False)