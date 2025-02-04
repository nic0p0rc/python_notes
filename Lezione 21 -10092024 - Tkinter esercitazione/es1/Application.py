import tkinter as tk

class Application(object):
    def __init__(self, parent):
        #etichetta bottoni
        self.etichetta = tk.Label(parent, text = "Bottoni",
                     #bg= "darkblue",
                     font=("Arial, 12"),
                     fg = "blue")
        #poszione etichetta bottoni
        self.etichetta.grid(row=0, column=2, padx=10, pady=10)

        #bottoni e posizione
        self.scritta_button = tk.Label(parent, text = "tk.Button")
        self.scritta_button.grid(row=1, column=2)

        self.button = tk.Button(parent, text = "cliccami!!!", font=("Arial, 10"), fg="red")
        self.button.grid(row=1, column=3)

        #seconda etichetta scelte
        self.etichetta2 = tk.Label(parent, text="Scelte",
                                  # bg= "darkblue",
                                  font=("Arial, 12"),
                                  fg="blue")
        #posizione etichetta scelte
        self.etichetta2.grid(row=0, column=0, padx=10, pady=10)

        #radio button
        self.radio1 = tk.Radiobutton(parent, text="opzione 1", value="opzione 1",)
        self.radio2 = tk.Radiobutton(parent, text="opzione 2", value="opzione 2",)
        self.radio3 = tk.Radiobutton(parent, text="opzione 3", value="opzione 3",)
        #posizione radio
        self.radio1.grid(row=1, column=0, padx=10)
        self.radio2.grid(row=2, column=0, padx=10)
        self.radio3.grid(row=3, column=0, padx=10)

        #ceck button
        self.ceck1 = tk.Checkbutton(parent, text="opzione 1")
        self.ceck2 = tk.Checkbutton(parent, text="opzione 2")
        self.ceck3 = tk.Checkbutton(parent, text="opzione 3")
        #posizione ceck
        self.ceck1.grid(row=1, column=1, padx=10)
        self.ceck2.grid(row=2, column=1, padx=10)
        self.ceck3.grid(row=3, column=1, padx=10)

        #etichetta 3 input box
        self.etichetta3 = tk.Label(parent, text="InputBox",
                                   # bg= "darkblue",
                                   font=("Arial, 12"),
                                   fg="blue")
        # posizione etichetta scelte
        self.etichetta3.grid(row=4, column=0, padx=10, pady=10)
        #casella testo
        self.scritta_button = tk.Label(parent, text="tk.Entry")
        self.scritta_button.grid(row=5, column=0)
        self.inputbox = tk.Entry(parent)
        self.inputbox.grid(row=5,column=1, padx=10)
