"""
La libreria `tkinter` in Python è utilizzata per creare interfacce grafiche (GUI). Fornisce un set completo di widget
come pulsanti, etichette, caselle di testo, finestre e altri strumenti per costruire applicazioni GUI.

Ecco alcuni degli utilizzi più comuni della libreria `tkinter`:

1. Creare una finestra principale.
2. Aggiungere widget come etichette, pulsanti e caselle di testo.
3. Gestire eventi come clic sui pulsanti.
4. Organizzare i layout con vari gestori di geometria (pack, grid, place).
"""

import tkinter as tk
from tkinter import messagebox

# 1. Creare una finestra principale
"""
La classe `Tk()` crea una finestra principale che serve da contenitore per i widget.
"""
root = tk.Tk()
root.title("Esempio Tkinter")
root.geometry("300x200")  # Imposta la dimensione della finestra

# 2. Aggiungere widget
"""
È possibile aggiungere vari widget come etichette, pulsanti e caselle di testo alla finestra.
"""
# Aggiungi un'etichetta
label = tk.Label(root, text="Benvenuto in Tkinter!", font=("Arial", 14))
label.pack(pady=10)  # Posiziona l'etichetta nella finestra (padding margine attorno)

# Aggiungi una casella di testo (Entry)
text_entry = tk.Entry(root, width=30)
text_entry.pack(pady=10)

# 3. Gestire eventi (pulsanti e azioni)
"""
Per gestire eventi come il clic su un pulsante, si può collegare una funzione di callback.
"""
def on_button_click():
    testo = text_entry.get()
    messagebox.showinfo("Messaggio", f"Hai scritto: {testo}")

# Aggiungi un pulsante
button = tk.Button(root, text="Mostra Messaggio", command=on_button_click)
button.pack(pady=10)

# 4. Organizzare i layout con pack, grid, place
"""
`pack()`, `grid()` e `place()` sono metodi per posizionare i widget all'interno della finestra.
- `pack()` organizza i widget in una direzione (alto, basso, sinistra, destra).
- `grid()` organizza i widget in una griglia.
- `place()` permette il posizionamento assoluto tramite coordinate.
"""
# Esempio di posizionamento con grid
tk.Label(root, text="Nome:", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=5)
'''padx: spaziatura orizzontale a sinistra e a destra del widget.
pady: spaziatura verticale sopra e sotto il widget.'''
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Cognome:", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=5)
entry_cognome = tk.Entry(root)
entry_cognome.grid(row=1, column=1, padx=10, pady=5)

# 5. Avviare il loop principale dell'applicazione
"""
La funzione `mainloop()` avvia il loop principale della GUI, che attende gli eventi e aggiorna la finestra.
"""
root.mainloop()

"""
Questo è un esempio base dell'utilizzo di `tkinter` per creare interfacce grafiche. 
Questa libreria offre una vasta gamma di widget e funzionalità per sviluppare applicazioni GUI più complesse.
"""
