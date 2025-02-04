"""
Un decorator è una funzione che prende un'altra funzione come argomento, aggiunge qualche tipo di funzionalità,
e poi restituisce una nuova funzione senza modificare il codice della funzione originale. I decorator sono 
spesso usati per aggiungere funzionalità come logging, controllo degli accessi, caching, ecc.

Nel seguente esempio base, definiamo un decorator chiamato `my_decorator`. Questa funzione prende una funzione 
come argomento (`func`) e definisce una funzione interna `wrapper` che aggiunge del codice prima e dopo la chiamata 
alla funzione originale. Infine, il decorator restituisce la funzione `wrapper` che verrà chiamata al posto della 
funzione originale.

Esempio base di un decorator:
"""
def my_decorator(func):
    def wrapper():
        print("Qualcosa è accaduto prima della chiamata alla funzione.")
        func()
        print("Qualcosa è accaduto dopo la chiamata alla funzione.")
    return wrapper

@my_decorator
def say_hello():
    print("Ciao!")

# Chiamare la funzione decorata
say_hello()

"""
Nel secondo esempio, modifichiamo il decorator per accettare una funzione che prende due argomenti e restituire 
il risultato moltiplicato per 2.
"""
def my_decorator(fun):
    def wrapper(a, b):
        ris = fun(a, b) * 2
        return ris
    return wrapper

@my_decorator
def mio_calcolo(x, y):
    return x + y

# Chiamare la funzione decorata con due argomenti
print(mio_calcolo(2, 5))

"""
Nel terzo esempio, rendiamo il decorator più flessibile utilizzando `*args` per accettare un numero variabile di 
argomenti. Il decorator moltiplicherà il risultato della funzione originale per 2, indipendentemente dal numero di 
argomenti.
"""
def my_decorator(fun):
    def wrapper(*a):
        ris = fun(*a) * 2
        return ris
    return wrapper

@my_decorator
def mio_calcolo(x, y):
    return x + y

# Chiamare la funzione decorata con due argomenti
print(mio_calcolo(2, 5))

@my_decorator
def mio_calcolo_1():
    return 5

# Chiamare la funzione decorata senza argomenti
print(mio_calcolo_1())

@my_decorator
def mio_calcolo_2(x, y, z):
    return x + y + z

# Chiamare la funzione decorata con tre argomenti
print(mio_calcolo_2(2, 5, 3))

"""
Nel quarto esempio, utilizziamo `functools.wraps` per mantenere i metadata della funzione originale 
(nome, docstring, ecc.). Questo è utile quando si vogliono preservare le informazioni della funzione originale.
"""
from functools import wraps

def my_decorator(fun):
    @wraps(fun)
    def wrapper(*a):
        ris = fun(*a) * 2
        return ris
    return wrapper

@my_decorator
def mio_calcolo(x, y):
    return x + y

# Chiamare la funzione decorata
print(mio_calcolo(2, 5))

# Accedere alla funzione originale senza decoratore
mia = mio_calcolo.__wrapped__
# Chiamare la funzione originale senza decoratore
print(mia(2, 5))
