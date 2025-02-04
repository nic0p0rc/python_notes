import tkinter as tk
'''
Spiegazione:
-Label: Mostra testo o immagini statiche, con opzioni per la formattazione del testo e il colore.
-Entry: Per input di testo a singola riga, con supporto per password e variabili di testo.
-Button: Pulsante interattivo con testo, comando associato e opzioni di formattazione.
-Text: Per testo multilinea, con opzioni di wrapping e dimensionamento.
-Checkbutton: Casella di controllo per selezionare opzioni multiple, con variabili associate.
-Radiobutton: Pulsanti di opzione per una selezione esclusiva tra opzioni, con variabili associate.
-Scale: Barra di scorrimento per selezionare valori numerici, con supporto per callback e visualizzazione del valore.
-Listbox: Elenco di opzioni con modalità di selezione multiple e supporto per aggiungere elementi.
-Canvas: Area di disegno per creare grafica personalizzata, con supporto per linee, rettangoli e cerchi.
Questo codice include commenti dettagliati per ciascun widget, illustrando come utilizzarli e quali parametri possono essere impostati.
'''

# Creazione della finestra principale
root = tk.Tk()
root.title("Esempio di Widget Tkinter")
root.geometry("400x900")

# --------------------- Label ---------------------
"""
La classe `Label` è utilizzata per visualizzare del testo o immagini statiche.

Parametri principali:
- `master`: La finestra o il contenitore in cui il widget deve essere inserito.

- `text`: Il testo da visualizzare nel widget.
  - Esempio: `text="Ciao, Mondo!"`

- `font`: Specifica il tipo e la dimensione del font.
  - Esempio: `font=("Arial", 12)`

- `bg` o `background`: Colore di sfondo del widget.
  - Esempio: `bg="lightblue"`

- `fg` o `foreground`: Colore del testo.
  - Esempio: `fg="black"`

- `width`: Larghezza del widget in caratteri.
  - Esempio: `width=20`

- `height`: Altezza del widget in righe di testo.
  - Esempio: `height=2`

- `anchor`: Specifica l'allineamento del testo all'interno del widget.
  - Valori: `tk.N`, `tk.S`, `tk.E`, `tk.W`, `tk.CENTER` (default)

- `padx` e `pady`: Spazio interno orizzontale e verticale.
  - Esempio: `padx=10`, `pady=5`
"""
label = tk.Label(root, text="Esempio di etichetta", font=("Arial", 12))
label.pack(pady=10)

# --------------------- Entry ---------------------
"""
La classe `Entry` è utilizzata per inserire una singola riga di testo.

Parametri principali:
- `master`: La finestra o il contenitore in cui il widget deve essere inserito.

- `width`: La larghezza del widget in caratteri.
  - Esempio: `width=30`

- `bg` o `background`: Colore di sfondo del widget.
  - Esempio: `bg="white"`

- `fg` o `foreground`: Colore del testo.
  - Esempio: `fg="black"`

- `font`: Specifica il tipo e la dimensione del font.
  - Esempio: `font=("Arial", 12)`

- `show`: Mostra i caratteri inseriti come un simbolo, utile per le password.
  - Esempio: `show="*"`

- `state`: Specifica lo stato del widget.
  - Valori: `tk.NORMAL` (default), `tk.DISABLED`

- `textvariable`: Variabile associata al widget per ottenere o impostare il testo.
  - Esempio: `textvariable=my_var`
"""
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# --------------------- Button ---------------------
"""
La classe `Button` è utilizzata per creare pulsanti che l'utente può cliccare.

Parametri principali:
- `master`: La finestra o il contenitore in cui il widget deve essere inserito.

- `text`: Il testo visualizzato sul pulsante.
  - Esempio: `text="Cliccami"`

- `command`: Funzione da chiamare quando il pulsante viene cliccato.
  - Esempio: `command=my_function`

- `bg` o `background`: Colore di sfondo del pulsante.
  - Esempio: `bg="lightgrey"`

- `fg` o `foreground`: Colore del testo.
  - Esempio: `fg="black"`

- `font`: Specifica il tipo e la dimensione del font.
  - Esempio: `font=("Arial", 12)`

- `width`: Larghezza del pulsante in caratteri.
  - Esempio: `width=10`

- `height`: Altezza del pulsante in righe di testo.
  - Esempio: `height=2`

- `padx` e `pady`: Spazio interno orizzontale e verticale.
  - Esempio: `padx=10`, `pady=5`

- `state`: Specifica lo stato del pulsante.
  - Valori: `tk.NORMAL` (default), `tk.DISABLED`
"""
button = tk.Button(root, text="Cliccami", command=lambda: print("Pulsante cliccato"))
button.pack(pady=10)

# --------------------- Text ---------------------
"""
La classe `Text` è utilizzata per inserire e modificare testo multilinea.

Parametri principali:
- `master`: La finestra o il contenitore in cui il widget deve essere inserito.

- `width`: La larghezza del widget in caratteri.
  - Esempio: `width=40`

- `height`: L'altezza del widget in righe di testo.
  - Esempio: `height=10`

- `bg` o `background`: Colore di sfondo del widget.
  - Esempio: `bg="white"`

- `fg` o `foreground`: Colore del testo.
  - Esempio: `fg="black"`

- `font`: Specifica il tipo e la dimensione del font.
  - Esempio: `font=("Arial", 12)`

- `padx` e `pady`: Spazio interno orizzontale e verticale.
  - Esempio: `padx=10`, `pady=5`

- `wrap`: Specifica come effettuare il wrapping del testo.
  - Valori: `tk.NONE` (default), `tk.CHAR`, `tk.WORD`
"""
text = tk.Text(root, width=40, height=10)
text.pack(pady=10)

# --------------------- Checkbutton ---------------------
"""
La classe `Checkbutton` è utilizzata per creare caselle di controllo.

Parametri principali:
- `master`: La finestra o il contenitore in cui il widget deve essere inserito.

- `text`: Il testo visualizzato accanto alla casella di controllo.
  - Esempio: `text="Opzione"`

- `variable`: Variabile associata al checkbutton, utile per ottenere o impostare il valore.
  - Esempio: `variable=my_var`

- `onvalue` e `offvalue`: Valori che la variabile assume quando il checkbutton è selezionato o deselezionato.
  - Esempio: `onvalue=1`, `offvalue=0`

- `bg` o `background`: Colore di sfondo del widget.
  - Esempio: `bg="white"`

- `fg` o `foreground`: Colore del testo.
  - Esempio: `fg="black"`

- `font`: Specifica il tipo e la dimensione del font.
  - Esempio: `font=("Arial", 12)`

- `padx` e `pady`: Spazio interno orizzontale e verticale.
  - Esempio: `padx=10`, `pady=5`
"""
checkbutton_var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Opzione", variable=checkbutton_var)
checkbutton.pack(pady=10)

# --------------------- Radiobutton ---------------------
"""
La classe `Radiobutton` è utilizzata per creare bottoni di opzione, dove solo una scelta può essere selezionata.

Parametri principali:
- `master`: La finestra o il contenitore in cui il widget deve essere inserito.

- `text`: Il testo visualizzato accanto al bottone di opzione.
  - Esempio: `text="Opzione 1"`

- `variable`: Variabile associata ai radiobuttons, utile per ottenere o impostare il valore selezionato.
  - Esempio: `variable=my_var`

- `value`: Il valore associato al bottone di opzione.
  - Esempio: `value=1`

- `bg` o `background`: Colore di sfondo del widget.
  - Esempio: `bg="white"`

- `fg` o `foreground`: Colore del testo.
  - Esempio: `fg="black"`

- `font`: Specifica il tipo e la dimensione del font.
  - Esempio: `font=("Arial", 12)`

- `padx` e `pady`: Spazio interno orizzontale e verticale.
  - Esempio: `padx=10`, `pady=5`
"""
radiobutton_var = tk.IntVar()
radiobutton1 = tk.Radiobutton(root, text="Opzione 1", variable=radiobutton_var, value=1)
radiobutton2 = tk.Radiobutton(root, text="Opzione 2", variable=radiobutton_var, value=2)
radiobutton1.pack(pady=5)
radiobutton2.pack(pady=5)

# --------------------- Scale ---------------------
"""
La classe `Scale` è utilizzata per creare una barra di scorrimento, utile per selezionare valori numerici.

Parametri principali:
- `master`: La finestra o il contenitore in cui il widget deve essere inserito.

- `from_`: Valore iniziale della scala (minimo).
  - Esempio: `from_=0`

- `to`: Valore finale della scala (massimo).
  - Esempio: `to=100`

- `orient`: Orientamento della scala.
  - Valori possibili: 
    - `tk.HORIZONTAL`: Scala orizzontale.
    - `tk.VERTICAL`: Scala verticale.

- `length`: Lunghezza della scala (solo per scale orizzontali) o altezza (solo per scale verticali).
  - Esempio: `length=200`

- `tickinterval`: Intervallo dei tick marks (linee di riferimento) sulla scala.
  - Esempio: `tickinterval=10`

- `resolution`: Risoluzione dei valori della scala (quantità di incremento).
  - Esempio: `resolution=1`

- `showvalue`: Se `True`, visualizza il valore corrente sopra la scala.
  - Esempio: `showvalue=True`

- `variable`: Variabile associata alla scala per ottenere o impostare il valore.
  - Esempio: `variable=my_var`

- `command`: Funzione di callback chiamata ogni volta che il valore cambia.
  - Esempio: `command=my_callback_function`
"""
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, length=300, tickinterval=10, resolution=1, showvalue=True)
scale.pack(pady=10)

# --------------------- Listbox ---------------------
"""
La classe `Listbox` è utilizzata per visualizzare una lista di opzioni tra cui l'utente può scegliere.

Parametri principali:
- `master`: La finestra o il contenitore in cui il widget deve essere inserito.

- `height`: Altezza della lista in righe.
  - Esempio: `height=5`

- `width`: Larghezza della lista in caratteri.
  - Esempio: `width=20`

- `bg` o `background`: Colore di sfondo del widget.
  - Esempio: `bg="white"`

- `fg` o `foreground`: Colore del testo.
  - Esempio: `fg="black"`

- `font`: Specifica il tipo e la dimensione del font.
  - Esempio: `font=("Arial", 12)`

- `selectmode`: Specifica il modo di selezione degli elementi.
  - Valori possibili:
    - `tk.SINGLE`: Solo un elemento può essere selezionato.
    - `tk.BROWSE`: Solo un elemento può essere selezionato, ma l'utente può sfogliare.
    - `tk.MULTIPLE`: Più elementi possono essere selezionati.
    - `tk.EXTENDED`: Selezione estesa (più elementi con selezione continua).

- `bg` o `background`: Colore di sfondo del widget.
  - Esempio: `bg="white"`

- `fg` o `foreground`: Colore del testo.
  - Esempio: `fg="black"`
"""
listbox = tk.Listbox(root, height=5, width=30)
listbox.pack(pady=10)
listbox.insert(tk.END, "Opzione 1")
listbox.insert(tk.END, "Opzione 2")
listbox.insert(tk.END, "Opzione 3")

# --------------------- Canvas ---------------------
"""
La classe `Canvas` è utilizzata per disegnare oggetti grafici come linee, cerchi, e rettangoli.

Parametri principali:
- `master`: La finestra o il contenitore in cui il widget deve essere inserito.

- `bg` o `background`: Colore di sfondo del canvas.
  - Esempio: `bg="white"`

- `width`: Larghezza del canvas.
  - Esempio: `width=200`

- `height`: Altezza del canvas.
  - Esempio: `height=200`

- `bd` o `borderwidth`: Larghezza del bordo del canvas.
  - Esempio: `bd=2`

- `relief`: Tipo di rilievo del bordo del canvas.
  - Valori possibili:
    - `tk.FLAT`: Senza rilievo.
    - `tk.RAISED`: Rilevato.
    - `tk.SUNKEN`: Incassato.
    - `tk.GROOVE`: Incassato con bordo in rilievo.
    - `tk.RIDGE`: Rilevato con bordo incassato.
"""
canvas = tk.Canvas(root, width=200, height=200, bg="white")
canvas.pack(pady=10)
canvas.create_line(10, 10, 190, 190, fill="black")
canvas.create_rectangle(50, 50, 150, 150, outline="blue", fill="lightblue")
canvas.create_oval(70, 70, 130, 130, outline="red", fill="pink")

# Avvio del loop principale dell'applicazione
root.mainloop()

