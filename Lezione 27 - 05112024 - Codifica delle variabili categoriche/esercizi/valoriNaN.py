import pandas as pd

df = pd.read_csv('esempio.csv')

#Primo metodo
'''fillna() questo metodo permette di sostituire i valori mancanti con un
valore specificato ad esempio un numero che vogliamo o come in questo caso la 
media della colonna
print(df["Età"])
df["Età"] = df["Età"].fillna(df["Età"].mean())
print(df["Età"])'''

#Secondo metodo
'''dropna() permette di rimuovere le riche o le colonne con valori mancanti
#riga
df_senza_na = df.dropna()
print(df_senza_na)
#colonna
df_senza_na = df.dropna(axis=1)
print(df_senza_na)'''

df["Età"] = df["Età"].fillna(df["Età"].mean())
df = df.dropna()
print(df)