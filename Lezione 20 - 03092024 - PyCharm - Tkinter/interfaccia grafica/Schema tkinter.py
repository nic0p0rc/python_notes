import tkinter as tk
from tkinter import messagebox

"""
Spiegazione:
1.Finestra principale (root): Crea e configura la finestra principale con titolo e dimensioni.
2.Widget: Crea un'etichetta, una casella di testo e un pulsante.
3.Layout (grid()): Posiziona i widget con il layout a griglia.
4.Gestione degli eventi: Associa al pulsante una funzione che mostra il testo inserito dall'utente in un popup.
5.Loop principale: Avvia il ciclo principale della GUI con mainloop().
Questo codice ti fornirà una GUI funzionante con un layout ordinato e la possibilità di interagire con i widget.
""""

# 1. Creazione della finestra principale (root)
"""
Il primo passo è creare la finestra principale.
Questa finestra è il contenitore di tutti i widget (come etichette, pulsanti, campi di testo, ecc.).
"""
root = tk.Tk()
root.title("Titolo della Finestra")  # Imposta il titolo della finestra
root.geometry("400x300")  # Imposta le dimensioni della finestra

# 2. Creazione e configurazione dei widget
"""
A questo punto puoi creare vari widget come etichette (Label),
pulsanti (Button), campi di testo (Entry), e altri. Ogni widget viene
istanziato ma non appare ancora nella finestra fino a quando non lo "posizioni".
"""
label = tk.Label(root, text="Inserisci il tuo nome:")
entry = tk.Entry(root)
button = tk.Button(root, text="Mostra Messaggio")

# 3. Posizionamento dei widget (gestione del layout)
"""
Dopo aver creato i widget, devi posizionarli nella finestra principale.
Ci sono tre principali gestori di geometria che ti permettono di posizionare i widget:
- pack(): Posiziona i widget in verticale o orizzontale, impilati uno sopra l'altro o accanto.
- grid(): Posiziona i widget in una griglia, con righe e colonne.
- place(): Posiziona i widget in base a coordinate assolute.
In questo esempio usiamo il layout `grid()`.
"""
label.grid(row=0, column=0, padx=10, pady=10)  # Posiziona l'etichetta
entry.grid(row=0, column=1, padx=10, pady=10)  # Posiziona la casella di testo
button.grid(row=1, column=0, columnspan=2, pady=20)  # Posiziona il pulsante

# 4. Gestione degli eventi e azioni
"""
Puoi collegare i widget (ad esempio un pulsante) a delle funzioni di callback
per gestire gli eventi. In questo caso, specifichiamo cosa deve accadere
quando l'utente clicca sul pulsante.
"""
def on_button_click():
    """
    Quando il pulsante viene cliccato, ottiene il testo inserito
    nell'Entry e lo stampa in una finestra di messaggio.
    """
    testo = entry.get()  # Ottieni il testo inserito nella casella di testo
    if testo:
        messagebox.showinfo("Messaggio", f"Hai scritto: {testo}")  # Mostra un messaggio con il testo
    else:
        messagebox.showwarning("Attenzione", "Inserisci un testo nel campo.")  # Avviso se il campo è vuoto

button.config(command=on_button_click)  # Collega il pulsante alla funzione `on_button_click`

# 5. Avvio del loop principale
"""
Dopo aver posizionato tutti i widget e configurato le azioni,
è necessario avviare il loop principale della finestra. Questo è il ciclo che
permette alla GUI di rimanere attiva e rispondere agli eventi (come clic, inserimenti, ecc.).
"""
root.mainloop()
