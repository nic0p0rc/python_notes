import tkinter as tk

root = tk.Tk()
root.title("Prima interfaccia") #titolo finestra
root.geometry("500x600+500+100") # 400x300 dimensioni finestra , +500+100 posizione xy

#scrivere nella finestra
etichetta = tk.Label(root, text = "Ciao a tutti ragazzi",
                     bg= "darkblue",
                     font=("Arial, 30"),
                     fg = "white",
                     width = 20,
                     pady = 30)
etichetta.grid(row=0, column=0, padx=10, pady=10)

#bottone
button = tk.Button(root, text = "cliccami", font=("Arial, 11"))
button.grid(row=1, column=0, padx=10, pady=10)

etichetta2 = tk.Label(root, text = "Arrivederci",
                      bg="darkblue",
                      font=("Arial, 20"),
                      fg="white",
                      width=10,
                      pady=20
                      )
etichetta2.grid(row=2, column=0, padx=10, pady=40)

#pulsante

root.mainloop()
