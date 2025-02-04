import tkinter as tk

'''
Spiegazione:

-pack(): Spiega i parametri per posizionare e configurare i widget in modo semplice e lineare.
-grid(): Dettaglia come disporre i widget in una griglia con righe e colonne e le opzioni per padding e allineamento.
-place(): Fornisce controllo preciso sul posizionamento dei widget con coordinate assolute e relative.

Questo codice include tutti i parametri che puoi utilizzare con ciascun metodo di gestione del layout, 
con spiegazioni chiare e dettagliate per ogni parametro.
'''

# Creazione della finestra principale
root = tk.Tk()
root.title("Esempio di Geometria Tkinter")
root.geometry("400x300")

# --------------------- pack() ---------------------
"""
Il metodo `pack()` organizza i widget all'interno di una finestra in modo verticale o orizzontale.

Parametri principali:
- `side`: Specifica su quale lato della finestra posizionare il widget.
  - Valori possibili: 
    - `tk.TOP` (default): Posiziona il widget in alto.
    - `tk.BOTTOM`: Posiziona il widget in basso.
    - `tk.LEFT`: Posiziona il widget a sinistra.
    - `tk.RIGHT`: Posiziona il widget a destra.

- `fill`: Determina se il widget deve estendersi per riempire lo spazio disponibile.
  - Valori possibili: 
    - `tk.NONE` (default): Il widget non si espande.
    - `tk.X`: Espande il widget orizzontalmente.
    - `tk.Y`: Espande il widget verticalmente.
    - `tk.BOTH`: Espande il widget sia in verticale che in orizzontale.

- `expand`: Se impostato su `True`, permette al widget di espandersi per occupare lo spazio non utilizzato nella finestra.
  - Valori possibili: 
    - `True`: Il widget si espande.
    - `False`: Il widget non si espande.

- `padx`: Aggiunge spazio (padding) orizzontale attorno al widget (a sinistra e a destra).
  - Esempio: `padx=10` aggiunge 10 pixel di spazio orizzontale.

- `pady`: Aggiunge spazio (padding) verticale attorno al widget (sopra e sotto).
  - Esempio: `pady=10` aggiunge 10 pixel di spazio verticale.

- `anchor`: Specifica dove ancorare il widget all'interno del suo spazio di contenimento.
  - Valori possibili: 
    - `tk.N`: Ancorato al bordo superiore.
    - `tk.S`: Ancorato al bordo inferiore.
    - `tk.E`: Ancorato al bordo destro.
    - `tk.W`: Ancorato al bordo sinistro.
    - `tk.NE`, `tk.NW`, `tk.SE`, `tk.SW`: Ancorato agli angoli.
    - `tk.CENTER` (default): Ancorato al centro.
"""
label = tk.Label(root, text="Esempio di etichetta")
label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10, expand=True)

# --------------------- grid() ---------------------
"""
Il metodo `grid()` organizza i widget in una griglia con righe e colonne.

Parametri principali:
- `row`: Specifica la riga in cui posizionare il widget.
  - Esempio: `row=0` posiziona il widget nella prima riga.

- `column`: Specifica la colonna in cui posizionare il widget.
  - Esempio: `column=0` posiziona il widget nella prima colonna.

- `rowspan`: Indica il numero di righe che il widget deve attraversare.
  - Esempio: `rowspan=2` permette al widget di occupare due righe.

- `columnspan`: Indica il numero di colonne che il widget deve attraversare.
  - Esempio: `columnspan=2` permette al widget di occupare due colonne.

- `padx`: Aggiunge spazio (padding) orizzontale attorno al widget (a sinistra e a destra).
  - Esempio: `padx=10` aggiunge 10 pixel di spazio orizzontale.

- `pady`: Aggiunge spazio (padding) verticale attorno al widget (sopra e sotto).
  - Esempio: `pady=10` aggiunge 10 pixel di spazio verticale.

- `sticky`: Specifica l'allineamento del widget all'interno della cella della griglia.
  - Valori possibili: 
    - `tk.N`: Allinea al bordo superiore.
    - `tk.S`: Allinea al bordo inferiore.
    - `tk.E`: Allinea al bordo destro.
    - `tk.W`: Allinea al bordo sinistro.
    - `tk.NE`, `tk.NW`, `tk.SE`, `tk.SW`: Allinea agli angoli.
    - `tk.CENTER`: Allinea al centro.

- `ipadx`: Aggiunge spazio interno orizzontale (padding) all'interno del widget.
  - Esempio: `ipadx=5` aggiunge 5 pixel di padding interno orizzontale.

- `ipady`: Aggiunge spazio interno verticale (padding) all'interno del widget.
  - Esempio: `ipady=5` aggiunge 5 pixel di padding interno verticale.
"""
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W, columnspan=2)

# --------------------- place() ---------------------
"""
Il metodo `place()` permette di posizionare i widget in una posizione esatta usando coordinate x e y.

Parametri principali:
- `x`: La coordinata orizzontale (in pixel) dove posizionare il widget.
  - Esempio: `x=50` posiziona il widget 50 pixel a sinistra.

- `y`: La coordinata verticale (in pixel) dove posizionare il widget.
  - Esempio: `y=50` posiziona il widget 50 pixel dall'alto.

- `relx`: Posiziona il widget come frazione della larghezza della finestra.
  - Esempio: `relx=0.5` posiziona il widget al centro orizzontale della finestra.

- `rely`: Posiziona il widget come frazione dell'altezza della finestra.
  - Esempio: `rely=0.5` posiziona il widget al centro verticale della finestra.

- `anchor`: Specifica il punto di ancoraggio del widget rispetto alla posizione (x, y).
  - Valori possibili: 
    - `tk.N`: Ancoraggio al bordo superiore.
    - `tk.S`: Ancoraggio al bordo inferiore.
    - `tk.E`: Ancoraggio al bordo destro.
    - `tk.W`: Ancoraggio al bordo sinistro.
    - `tk.CENTER` (default): Ancoraggio al centro.

- `width`: Imposta la larghezza del widget in pixel.
  - Esempio: `width=150` imposta la larghezza a 150 pixel.

- `height`: Imposta l'altezza del widget in pixel.
  - Esempio: `height=50` imposta l'altezza a 50 pixel.

- `relwidth`: Imposta la larghezza come frazione della larghezza della finestra.
  - Esempio: `relwidth=0.5` imposta la larghezza del widget al 50% della larghezza della finestra.

- `relheight`: Imposta l'altezza come frazione dell'altezza della finestra.
  - Esempio: `relheight=0.3` imposta l'altezza del widget al 30% dell'altezza della finestra.
"""
button = tk.Button(root, text="Pulsante")
button.place(x=100, y=150, width=150, height=50)

# Avvio del loop principale dell'applicazione
root.mainloop()
