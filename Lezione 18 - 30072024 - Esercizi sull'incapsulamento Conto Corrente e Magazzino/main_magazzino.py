import class_magazzino
pomodoro = class_magazzino.Magazzino("pom", "rosso", 1, 7)
print(pomodoro)
print(pomodoro.ordine())
print(pomodoro.cliente(6))
print(pomodoro.acquisto(10))