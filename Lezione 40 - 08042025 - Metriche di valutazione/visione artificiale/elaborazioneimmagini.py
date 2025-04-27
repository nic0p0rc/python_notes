# Importiamo la libreria OpenCV, che ci permette di elaborare immagini e video
import cv2

# Importiamo Matplotlib, una libreria per creare grafici e visualizzare immagini
import matplotlib.pyplot as plt

# ---------------------------------------------------
# Caricamento dell'immagine in scala di grigi
# cv2.imread serve per leggere un'immagine dal file system.
# cv2.IMREAD_GRAYSCALE indica che vogliamo caricare l'immagine in bianco e nero (scala di grigi)
# ---------------------------------------------------
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# ---------------------------------------------------
# Ridimensionamento dell'immagine
# cv2.resize serve a cambiare la dimensione di un'immagine.
# Qui stiamo ridimensionando l'immagine a 100x100 pixel.
# ---------------------------------------------------
resized_image = cv2.resize(image, (100, 100))

# ---------------------------------------------------
# Riduzione del rumore nell'immagine
# cv2.GaussianBlur applica un filtro di sfocatura Gaussiana.
# Serve per ridurre il rumore e rendere più morbide le transizioni tra colori o intensità.
# (5,5) indica la dimensione del filtro (un quadrato 5x5 pixel).
# 0 indica la deviazione standard della distribuzione gaussiana (calcolata automaticamente).
# NB: Qui stiamo sfocando l'immagine originale, non quella ridimensionata.
# ---------------------------------------------------
denoised_image = cv2.GaussianBlur(image, (5, 5), 0)

# ---------------------------------------------------
# Rilevamento dei bordi nell'immagine
# cv2.Canny è un algoritmo che individua i contorni (edge detection).
# 100 è il valore di soglia minima, 200 è la soglia massima: controllano la sensibilità del rilevamento.
# Rileviamo i contorni sull'immagine originale.
# ---------------------------------------------------
edges = cv2.Canny(image, 100, 200)

# ---------------------------------------------------
# Visualizzazione delle immagini
# Creiamo una finestra di figura grande 10x8 pollici.
# Poi dividiamo la finestra in una griglia 2x2 e mostriamo:
# - l'immagine originale
# - l'immagine ridimensionata
# - l'immagine denoised
# - i bordi rilevati
# cmap='gray' dice a matplotlib di usare una mappa di colori in scala di grigi.
# ---------------------------------------------------
plt.figure(figsize=(10, 8))

# Mostriamo l'immagine originale
plt.subplot(2, 2, 1)  # 2 righe, 2 colonne, primo riquadro
plt.imshow(image, cmap='gray')
plt.title('Original Image')

# Mostriamo l'immagine ridimensionata
plt.subplot(2, 2, 2)  # 2 righe, 2 colonne, secondo riquadro
plt.imshow(resized_image, cmap='gray')
plt.title('Resized Image')

# Mostriamo l'immagine denoised
plt.subplot(2, 2, 3)  # 2 righe, 2 colonne, terzo riquadro
plt.imshow(denoised_image, cmap='gray')
plt.title('Denoised Image')

# Mostriamo i bordi rilevati
plt.subplot(2, 2, 4)  # 2 righe, 2 colonne, quarto riquadro
plt.imshow(edges, cmap='gray')
plt.title('Edges')

# Visualizziamo la finestra
plt.show()
