"""
Su pyhon.org --> https://docs.python.org/3/library/os.html

La libreria `os` in Python fornisce una serie di funzioni per interagire con il sistema operativo. È particolarmente
utile per operazioni come la gestione dei file e delle directory, l'esecuzione di comandi di sistema, la gestione
delle variabili d'ambiente e molto altro.

Ecco alcuni degli utilizzi più comuni della libreria `os`:

1. Ottenere il percorso della directory corrente.
2. Cambiare la directory corrente.
3. Creare nuove directory.
4. Listare i file in una directory.
5. Rimuovere file e directory.
6. Ottenere e impostare variabili d'ambiente.
7. Eseguire comandi di sistema.
"""

import os

# 1. Ottenere il percorso della directory corrente
"""
La funzione `os.getcwd()` restituisce il percorso della directory di lavoro corrente.
"""
current_directory = os.getcwd()
print(f"Directory corrente: {current_directory}")

# 2. Cambiare la directory corrente
"""
La funzione `os.chdir(path)` cambia la directory di lavoro corrente. 
Qui cambiamo alla directory precedente (un livello sopra).
"""
os.chdir('..')
print(f"Directory dopo os.chdir('..'): {os.getcwd()}")

# Torna alla directory originale
os.chdir(current_directory)

# 3. Creare nuove directory
"""
La funzione `os.mkdir(path)` crea una nuova directory con il nome specificato. 
La funzione `os.makedirs(path)` può creare directory intermedie nel percorso, se necessario.
"""
new_dir = "nuova_directory"
os.mkdir(new_dir)
print(f"Directory '{new_dir}' creata.")

# Pulizia: rimuovere la directory appena creata
os.rmdir(new_dir)

# 4. Listare i file in una directory
"""
La funzione `os.listdir(path)` restituisce un elenco di tutti i file e le directory nel percorso specificato.
Se nessun percorso è specificato, viene utilizzata la directory corrente.
"""
files_and_dirs = os.listdir('.')
print(f"Contenuti della directory corrente: {files_and_dirs}")

# 5. Rimuovere file e directory
"""
La funzione `os.remove(path)` rimuove un file. 
La funzione `os.rmdir(path)` rimuove una directory vuota.
La funzione `os.removedirs(path)` rimuove directory e, se necessario, directory superiori vuote.
"""
# Creare un file di esempio
with open("test_file.txt", "w") as f:
    f.write("Questo è un file di test.")
print("File 'test_file.txt' creato.")

# Rimuovere il file creato
os.remove("test_file.txt")
print("File 'test_file.txt' rimosso.")

# Creare una directory di esempio
os.mkdir("test_directory")
print("Directory 'test_directory' creata.")

# Rimuovere la directory creata
os.rmdir("test_directory")
print("Directory 'test_directory' rimossa.")

# 6. Ottenere e impostare variabili d'ambiente
"""
La funzione `os.getenv(key, default=None)` restituisce il valore della variabile d'ambiente specificata.
La funzione `os.environ[key]` può anche essere usata per ottenere il valore della variabile d'ambiente.
La funzione `os.environ[key] = value` imposta una variabile d'ambiente.
"""
path_env = os.getenv('PATH')
print(f"Valore della variabile d'ambiente PATH: {path_env}")

# Impostare una nuova variabile d'ambiente
os.environ['MY_VAR'] = 'my_value'
print(f"Valore della variabile d'ambiente MY_VAR: {os.environ['MY_VAR']}")

# 7. Eseguire comandi di sistema
"""
La funzione `os.system(command)` esegue il comando del sistema specificato. 
Restituisce un valore di stato che indica il successo o il fallimento del comando.
"""
os.system('echo "Esegui un comando di sistema"')

"""
Questi sono alcuni degli utilizzi più comuni della libreria `os`. Questa libreria offre molte altre funzioni utili
per l'interazione con il sistema operativo e la gestione dei file e delle directory.
"""
