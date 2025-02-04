def main():
    testo = "\nnuovo testo da inserire in file"
    file = open("nicolo.txt", "a")
    file.write(testo)
    file.close()
    #sempre chiudere file per evitare con problemi con porte aperte che scansionano gli hacker

if __name__ == "__main__":
    main()