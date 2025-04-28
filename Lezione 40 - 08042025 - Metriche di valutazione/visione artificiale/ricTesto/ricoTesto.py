import pytesseract
from PIL import Image

# Dì a pytesseract dove trovare il file tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Caricamento dell'immagine
image = Image.open('text_image.jpg')

#riconoscimento del testo
text = pytesseract.image_to_string(image)

print("Testo riconosciuto")
print(text)
