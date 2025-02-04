import prova_pandas as pd

dati= pd.DataFrame({
    'Colori':['Arancione','Blu','Arancione','Celeste','Bordeaux','Blu']
})

encoded_data= pd.get_dummies(dati, columns=['Colori'])

print("Dati codificati:")
print(encoded_data)