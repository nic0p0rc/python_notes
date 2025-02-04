import class_studente 

studente1 = class_studente.Studente("Mario","Verdi","001")
studente2 = class_studente.Studente("Giacomo","Rossi","002")

print(studente1)
#print(studente1.__nome)
print(studente1.getNome())
studente1.setNome("giorgio")
print(studente1.getNome("nik"))
