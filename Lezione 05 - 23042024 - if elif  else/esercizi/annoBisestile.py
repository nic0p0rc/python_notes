
anno = int(input("Inserire l'anno: "))

if anno %100 == 0 and anno %400 == 0:
    print(f"il {anno} è bisestile")
elif anno %100 != 0 and anno %4 == 0:
    print(f"il {anno} è bisestile")
else:
    print(f"il {anno} non è bisestile")