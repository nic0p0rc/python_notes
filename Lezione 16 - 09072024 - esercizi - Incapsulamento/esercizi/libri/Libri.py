class Libro:
    def __init__(self, titolo, autore, anno, categoria):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.categoria = categoria
        
    def caratteristiche(self):
        return f"{self.titolo} è un libro della categoria {self.categoria} scritto nel {self.anno} da {self.autore}\n"