import numpy
import pandas
from sklearn.feature_selection import SelectKBest
#from funzioni.funzioni import

'''Importare un modello di regressione o classificazione (ad esempio, LinearRegression per regressione lineare o 
LogisticRegression per classificazione logistica)'''
from sklearn.linear_model import LinearRegression

def creadataset():
    #Numero di osservazioni nel DataFrame
    numero_osservazioni = 100

    #Creare on dizionario vuoto per le colonne del DataFrame
    colonne = {}

    #Generare 20 caratteristiche casuali
    for i in range(20):
            #Generare valori casuali per ciascuna caratteristica
            colonne[f'Caratteristica {i+1}'] = numpy.random.randint(1,101, size=numero_osservazioni)

    #Generare valori casuali per il target
    colonne['Target'] = numpy.random.randint(0, 2, size =numero_osservazioni)

    #Creare il DataFrame utilizzando il dizionario di colonne
    dati = pandas.DataFrame(colonne)
    #Visualizzare le prime righe del DataFrame
    #print(dati)
    return dati

'''Creare un modello di regressione o classificazione (ad esempio, LinearRegression per regressione lineare o 
LogisticRegression per classificazione logistica)'''
modello = LinearRegression()

dati =creadataset()

X = dati.drop(columns=['Target'])
y = dati['Target']
'''Inizializzare il selettore con il numero desiderato
di caratteristiche da selezionare (k=10 nel nostro esempio)'''

selettore = SelectKBest(k=10)

#Addestrare il selettore sui dati X e i target y
caratteristiche_selezionate = selettore.fit_transform(X, y)

#Addestrare il modello utilizzando solo le caratteristiche selezionate
modello.fit(caratteristiche_selezionate, y)
print("caratteristiche selezionate")
print(caratteristiche_selezionate)

'''calcola il coefficiente di correlazione di Pearson per ciascuna caratteristica
ispetto al target e restituisce i nomi delle caratteristiche in ordine di rilevanza'''
caratteristiche_selezionate = test_statistico(X, y)
print("Caratteristiche selezionate:", caratteristiche_selezionate)

