frase= input("inserisci una frase: ")
spazi = frase.count(" ")
print(f"""
caratteri(spazi inclusi): {len(frase)}
caratteri(spazi esclusi): {len(frase)-spazi}
spazi: {spazi}""")
