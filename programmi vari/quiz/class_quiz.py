class Quiz:
    def __init__(self, domanda, opzioni, risposta_corretta):
        self.domanda = domanda  # Testo della domanda
        self.opzioni = opzioni   # Possibili risposte
        self.risposta_corretta = risposta_corretta  # Risposte corrette (es: 'b' e 'B')

    def mostra_domanda(self):
        print(self.domanda)
        for lettera, opzione in zip('abcd', self.opzioni):
            print(f"{lettera}) {opzione}")
        return input("Your answer: ")

    def verifica_risposta(self, risposta):
        if risposta.upper() in self.risposta_corretta:
            print("Corretto!\n")
            return True
        else:
            print(f"Sbagliato! La risposta corretta è '{self.risposta_corretta[0]}'.\n")
            return False