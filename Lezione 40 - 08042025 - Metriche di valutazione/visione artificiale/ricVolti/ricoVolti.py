import cv2
import matplotlib.pyplot as plt

#Caricamento del classificatore pre-addestrato per il riconoscimento dei volti
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Caricamento dell'immagine
image = cv2.imread('image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Riconoscimento dei volti
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#Visualizzazione dei risultati
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w,y+h), (255, 0, 0), 2)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Face Detection with OpenCV')
plt.show()