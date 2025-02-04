class Persona:
    def __init__(self, nome, cognome, annonascita):
        self.nome=nome
        self.cognome=cognome
        self.annonascita=annonascita
    def stampa(self):
        return f"Scheda persona\n{self.nome}\n{self.cognome}\n{self.annonascita}\n"

"""
Introduzione alla programmazione orientata agli oggetti (OOP)

La programmazione orientata agli oggetti è un paradigma di programmazione basato sui concetti di "oggetti", 
che possono contenere dati sotto forma di campi (spesso noti come attributi o proprietà) e codice sotto forma 
di procedure (spesso noti come metodi). Gli oggetti sono istanze di classi.

Ecco alcuni concetti fondamentali dell'OOP:
1. Classe
2. Oggetto
3. Istanza
4. Costruttori
5. Metodi
6. Parametro self
7. Modifica e eliminazione delle proprietà di un oggetto
8. Eliminazione di un oggetto
"""

"""
1. Creare una classe

Una classe è un modello per creare oggetti. Definisce un set di attributi e metodi comuni a tutti gli oggetti 
di quel tipo. La sintassi di base per definire una classe in Python è:
"""

class Persona:
    """
    Questa è una classe semplice chiamata 'Persona'.
    Rappresenta una persona con un nome e un'età.
    """
    pass  # La parola chiave 'pass' indica che la classe è vuota per ora

"""
2. Creare un oggetto

Un oggetto è un'istanza di una classe. Quando si crea un oggetto, si chiama il costruttore della classe.
"""

# Creazione di un oggetto della classe Persona
persona1 = Persona()

"""
3. Cos'è un'istanza

Un'istanza è un singolo oggetto creato da una classe. La creazione di un'istanza implica la chiamata del 
costruttore della classe, che può inizializzare gli attributi dell'oggetto.
"""

# Verifica che persona1 è un'istanza della classe Persona
print(isinstance(persona1, Persona))  # Stampa: True

"""
4. Costruttori

Il costruttore è un metodo speciale chiamato __init__ in Python. Viene chiamato automaticamente quando si crea 
un nuovo oggetto della classe. Può essere utilizzato per inizializzare gli attributi dell'oggetto.
"""

class Persona:
    """
    Questa è una classe chiamata 'Persona'.
    """
    def __init__(self, nome, età):
        """
        Questo è il costruttore della classe. Inizializza gli attributi nome ed età.
        """
        self.nome = nome
        self.età = età

# Creazione di un oggetto della classe Persona con nome ed età
persona2 = Persona("Alice", 30)
print(persona2.nome)  # Stampa: Alice
print(persona2.età)   # Stampa: 30

"""
5. Metodi

I metodi sono funzioni definite all'interno di una classe. Possono operare sugli attributi dell'oggetto e 
fornire funzionalità aggiuntive.
"""

class Persona:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età

    def saluta(self):
        """
        Questo è un metodo della classe Persona. Stampa un saluto utilizzando l'attributo nome.
        """
        print(f"Ciao, mi chiamo {self.nome} e ho {self.età} anni.")

# Creazione di un oggetto della classe Persona e chiamata al metodo saluta
persona3 = Persona("Bob", 25)
persona3.saluta()  # Stampa: Ciao, mi chiamo Bob e ho 25 anni.

"""
6. Parametro self

Il parametro self è una convenzione utilizzata nei metodi delle classi per riferirsi all'istanza corrente dell'oggetto. 
Permette di accedere agli attributi e ai metodi dell'oggetto.
"""

class Persona:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età

    def aggiorna_età(self, nuova_età):
        """
        Questo metodo aggiorna l'età dell'oggetto Persona.
        """
        self.età = nuova_età

# Creazione di un oggetto della classe Persona e aggiornamento dell'età
persona4 = Persona("Charlie", 40)
persona4.aggiorna_età(41)
print(persona4.età)  # Stampa: 41

"""
7. Come modificare, eliminare le proprietà di un oggetto

È possibile modificare gli attributi di un oggetto direttamente o tramite metodi. È anche possibile eliminare 
un attributo utilizzando la funzione del.
"""

# Modifica dell'attributo nome
persona4.nome = "Charlie Brown"
print(persona4.nome)  # Stampa: Charlie Brown

# Eliminazione dell'attributo età
del persona4.età
# print(persona4.età)  # Questo genererebbe un errore perché l'attributo età è stato eliminato

"""
8. Come eliminare un oggetto

È possibile eliminare un oggetto utilizzando la funzione del. Questo rimuove l'oggetto dalla memoria.
"""

# Creazione di un nuovo oggetto Persona
persona5 = Persona("David", 50)

# Eliminazione dell'oggetto persona5
del persona5
# print(persona5)  # Questo genererebbe un errore perché l'oggetto persona5 è stato eliminato

"""
Questi appunti coprono i concetti fondamentali della programmazione orientata agli oggetti in Python, inclusi 
classe, oggetto, istanza, costruttori, metodi, parametro self, e come modificare o eliminare proprietà e oggetti.
"""
