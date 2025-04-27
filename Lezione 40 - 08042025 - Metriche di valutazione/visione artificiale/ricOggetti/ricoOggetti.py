import cv2
import numpy as np
import matplotlib.pyplot as plt

#Caricamento del modello YOLO
net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

#Caricamento dell'immagine
image = cv2.imread('persone.jpg')
height, width = image.shape[:2]

#Preprocessamento dell'immagine
image_resized = cv2.resize(image, (416, 416)) # aggiunta
blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput (blob)
outs = net.forward(output_layers)

#Estrazione delle informazioni sugli oggetti rilevati
class_ids = []
confidences = []
boxes = []

for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0] *width)
            center_y = int(detection[1] *height)
            w = int(detection[2] *width)
            h = int(detection[3] *height)
            x = int(center_x - w/2)
            y = int(center_y - h/2)
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

#Appisonsione di Mon-Maximum Suppression
indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5,0.4)

#Visualizzazione del risultati
for i in indices:
    box = boxes[i]
    x, y, w, h = box[0], box[1], box [2], box [3]
    cv2.rectangle(image, (x,y), (x + w, y + h), (0,255,0), 2)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Object Detection with TOLO')
plt.show()
