"""
La libreria `pyttsx3` in Python è utilizzata per la sintesi vocale, permettendo di convertire il testo in parlato. 
È un'interfaccia offline che supporta vari motori di sintesi vocale come SAPI5 su Windows, NSSpeechSynthesizer su MacOS 
e espeak su Unix.

Ecco alcuni degli utilizzi più comuni della libreria `pyttsx3`:

1. Configurare e inizializzare il motore di sintesi vocale.
2. Impostare le proprietà della voce come velocità, volume e voce specifica.
3. Convertire il testo in parlato.
4. Salvare il parlato generato in un file audio.
"""

import pyttsx3

# 1. Configurare e inizializzare il motore di sintesi vocale
"""
La funzione `pyttsx3.init()` inizializza il motore di sintesi vocale.
"""
engine = pyttsx3.init()

# 2. Impostare le proprietà della voce
"""
È possibile impostare diverse proprietà della voce come velocità, volume e voce specifica utilizzando `setProperty`.
"""
# Impostare la velocità del parlato (predefinito: 200 parole al minuto)
rate = engine.getProperty('rate')
print(f"Velocità corrente: {rate}")
engine.setProperty('rate', 150)

# Impostare il volume del parlato (predefinito: 1.0)
volume = engine.getProperty('volume')
print(f"Volume corrente: {volume}")
engine.setProperty('volume', 0.9)

# Impostare la voce specifica
"""
È possibile scegliere tra le voci disponibili e impostarne una specifica.
"""
voices = engine.getProperty('voices')
for voice in voices:
    print(f"ID: {voice.id}, Name: {voice.name}, Languages: {voice.languages}, Gender: {voice.gender}, Age: {voice.age}")

# Impostare la voce maschile (esempio)
engine.setProperty('voice', voices[0].id)

# 3. Convertire il testo in parlato
"""
La funzione `say` aggiunge il testo alla coda di parlato e `runAndWait` esegue il parlato.
"""
text = "Ciao, come stai?"
engine.say(text)
engine.runAndWait()

# 4. Salvare il parlato generato in un file audio
"""
La funzione `save_to_file` permette di salvare il parlato generato in un file audio.
"""
text_to_save = "Questo è un esempio di sintesi vocale salvato in un file audio."
engine.save_to_file(text_to_save, 'output_audio.mp3')
engine.runAndWait()

"""
Questi sono alcuni degli utilizzi più comuni della libreria `pyttsx3`. Questa libreria è estremamente utile per
applicazioni che richiedono sintesi vocale offline, come assistenti vocali, lettori di schermo e altre applicazioni
interattive.
"""
