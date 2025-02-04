from class_pilota import Pilota
from class_gara import Gara
from class_auto import Auto 


piloti = [
    Pilota("Mario","Rossi"),
    Pilota("Pippo","Verdi"),
    Pilota("Topolino","Giallo"),
    Pilota("Tizio","Caio"),
]

auto = [
    Auto("Ferrari", piloti[0], 0),
    Auto("RedBull", piloti[1], 1),
    Auto("Mercedes", piloti[2], 2),
    Auto("McLaren", piloti[3], 3),
]

def test():
    numero_giri = 5
    gara = Gara(numero_giri, auto)
    gara.simula_gara()

if __name__ == "__main__":
    test()