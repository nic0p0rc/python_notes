"""
Su python.org --> https://docs.python.org/3/library/html.html

La libreria `html` in Python fornisce funzioni utili per la manipolazione e l'escape di stringhe HTML. 
È particolarmente utile quando si lavora con HTML dinamico per prevenire attacchi di iniezione di codice 
o per decodificare entità HTML.

Ecco alcuni degli utilizzi più comuni della libreria `html`:

1. Escapare caratteri speciali in HTML.
2. Decodificare entità HTML.
3. Escapare e decodificare URL.
"""

import html

# 1. Escapare caratteri speciali in HTML
"""
La funzione `html.escape(string, quote=True)` sostituisce i caratteri speciali in `string` con le relative entità HTML.
"""
stringa_html = '<div class="content">Hello & welcome!</div>'
stringa_escape = html.escape(stringa_html)
print(f"Stringa escapata: {stringa_escape}")

# Escapare anche le virgolette
stringa_escape_quote = html.escape(stringa_html, quote=True)
print(f"Stringa escapata con virgolette: {stringa_escape_quote}")

# 2. Decodificare entità HTML
"""
La funzione `html.unescape(string)` converte le entità HTML in caratteri speciali.
"""
stringa_con_entita = 'The price is &euro;100'
stringa_decodificata = html.unescape(stringa_con_entita)
print(f"Stringa decodificata: {stringa_decodificata}")

# 3. Escapare e decodificare URL
"""
Per l'escape e la decodifica di URL, Python fornisce le funzioni `quote` e `unquote` dal modulo `urllib.parse`.
"""
import urllib.parse

url = 'https://www.example.com/?name=John Doe&age=30'
url_escape = urllib.parse.quote(url)
print(f"URL escapato: {url_escape}")

url_decodificato = urllib.parse.unquote(url_escape)
print(f"URL decodificato: {url_decodificato}")

"""
Questi sono alcuni degli utilizzi più comuni della libreria `html`. Le funzioni di escape e decodifica sono 
particolarmente utili quando si lavora con HTML dinamico o quando si ricevono input dagli utenti che devono 
essere inseriti in un contesto HTML in modo sicuro.
"""
