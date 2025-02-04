import  class_quiz


def main():
    score = 0

    domande = [
        class_quiz.Quiz("What does 'CPU' stand for?",
             ["Central Process Unit", "Central Processing Unit", "Central Performance Unit", "Core Process Unit"], 'B'),
        class_quiz.Quiz("Which of the following is not a programming language?",
             ["Python", "HTML", "Java", "C++"], 'B'),
        class_quiz.Quiz("How many bits does a byte consist of?",
             ["2", "4", "7", "8"], 'D'),
        class_quiz.Quiz("Which one is an example of an open-source operating system?",
             ["Windows", "macOS", "Linux", "DOS"], 'C'),
        class_quiz.Quiz("In C++, which symbol is used to comment a single line?",
             ["//", "##", "/* */", "<!-- -->"], 'A')
    ]

    num_domande = len(domande)

    for domanda in domande:
        risposta = domanda.mostra_domanda()
        if domanda.verifica_risposta(risposta):
            score += 1

    print(f"Il tuo punteggio è {score} su {num_domande}.")

    if score == num_domande:
        print("Eccellente, hai risposto correttamente a tutte le domande!")
    elif score >= 3:
        print("Hai passato il quiz.")
    else:
        print("Hai bisogno di più allenamento.")


if __name__ == "__main__":
    main()
