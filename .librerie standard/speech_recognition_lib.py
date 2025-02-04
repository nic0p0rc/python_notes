"""
La libreria `speech_recognition` in Python è utilizzata per riconoscere e trascrivere il parlato. 
Questa libreria fornisce una semplice interfaccia per diverse API di riconoscimento vocale e motori 
di riconoscimento vocale offline.

Ecco alcuni degli utilizzi più comuni della libreria `speech_recognition`:

1. Riconoscere il parlato da un file audio.
2. Riconoscere il parlato dal microfono.
3. Utilizzare diversi motori di riconoscimento vocale.
"""

import speech_recognition as sr

# 1. Riconoscere il parlato da un file audio
"""
La funzione `recognize_google(audio)` utilizza l'API di Google per riconoscere il parlato in un file audio.
"""
def riconoscere_da_file(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)  # Legge l'audio dal file
    try:
        testo = recognizer.recognize_google(audio)
        print(f"Testo riconosciuto dal file audio: {testo}")
    except sr.UnknownValueError:
        print("Google Speech Recognition non ha capito l'audio.")
    except sr.RequestError as e:
        print(f"Errore nella richiesta a Google Speech Recognition; {e}")

# Esempio di utilizzo
audio_file = "path/to/your/audiofile.wav"
riconoscere_da_file(audio_file)

# 2. Riconoscere il parlato dal microfono
"""
La funzione `recognize_google(audio)` utilizza l'API di Google per riconoscere il parlato dal microfono.
"""
def riconoscere_da_microfono():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Parla qualcosa...")
        audio = recognizer.listen(source)  # Registra l'audio dal microfono
    try:
        testo = recognizer.recognize_google(audio)
        print(f"Testo riconosciuto dal microfono: {testo}")
    except sr.UnknownValueError:
        print("Google Speech Recognition non ha capito l'audio.")
    except sr.RequestError as e:
        print(f"Errore nella richiesta a Google Speech Recognition; {e}")

# Esempio di utilizzo
# riconoscere_da_microfono()

# 3. Utilizzare diversi motori di riconoscimento vocale
"""
La libreria `speech_recognition` supporta diversi motori di riconoscimento vocale oltre a Google. 
Alcuni di questi includono Sphinx (offline), Bing, Houndify, IBM, e Wit.ai.
"""
def riconoscere_con_sphinx(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)  # Legge l'audio dal file
    try:
        testo = recognizer.recognize_sphinx(audio)
        print(f"Testo riconosciuto da Sphinx: {testo}")
    except sr.UnknownValueError:
        print("Sphinx non ha capito l'audio.")
    except sr.RequestError as e:
        print(f"Errore nella richiesta a Sphinx; {e}")

# Esempio di utilizzo
# riconoscere_con_sphinx(audio_file)

"""
Questi sono alcuni degli utilizzi più comuni della libreria `speech_recognition`. Questa libreria 
offre molte altre funzionalità e supporta diversi motori di riconoscimento vocale, rendendola 
flessibile e potente per applicazioni di riconoscimento vocale.
"""
