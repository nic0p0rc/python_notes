import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Creazione di un modello di rete neurale semplice
model = Sequential ([
    Dense (10, input_shape=(4,), activation= 'relu'), #Strato di input e nascosto
    Dense (5, activation= 'relu'), # Strato nascosto
    Dense (3, activation='softmax') # Strato di output
])

#Compilazione del modello
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#Visualizzazione del modello
model.summary()

#Addestramento del modello con dati di esempio
import numpy as np
X_train = np.random.rand(100,4)
y_train = np.random.randint(0,3,100)
history = model.fit(X_train, y_train, epochs=10, batch_size=10)

#Visualizzazione della loss durante l'addrestramento
import matplotlib.pyplot as plt
plt.plot(history.history['loss'])
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss durante l\'addestramento')
plt.show()