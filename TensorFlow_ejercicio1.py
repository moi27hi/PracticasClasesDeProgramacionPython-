import tensorflow as tf
import keras as ks
import numpy as np
import matplotlib.pyplot as plt




mnist = ks.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images / 255.0
test_images = test_images / 255.0


modelo = ks.Sequential([
    ks.layers.Flatten(input_shape=(28, 28)),
    ks.layers.Dense(128, activation='relu'),
    ks.layers.Dense(10, activation='softmax')
])

modelo.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

modelo.fit(train_images, train_labels, epochs=5) #Podemos cambiar el numero de epochs


predicciones = modelo.predict(test_images)
indice = 0
print(f'Etiqueta a identificar: {test_labels[indice]}')
print('Prediccion: ', np.argmax(predicciones[indice]))


plt.figure()
plt.imshow(test_images[indice])
plt.title(f"Prediccion: {np.argmax([predicciones[indice]])}")
plt.axis('off')
plt.show()