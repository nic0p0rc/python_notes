def main():
    testo = "\nciao a tutti ragazzi"
    with open("andrea.txt", "a") as file:
        file.write(testo)
    #non c'è necessita di chiudere quando si utilizza with open()...

if __name__ == "__main__":
    main()