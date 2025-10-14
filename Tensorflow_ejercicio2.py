import tensorflow as tf
import keras
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

mnist = keras.datasets.mnist
(train_images, train_labels),(test_images, test_labels) = mnist.load_data()

train_images = train_images/255.0
test_images = test_images/255.0

modelo = keras.Sequential([
    keras.layers.Flatten(input_shape = (28,28)),  #Solo la primera neurona es Flatten las demas son Dense
    keras.layers.Dense(128,activation="relu"),
    keras.layers.Dense(10,activation="softmax")
])

modelo.compile(optimizer="adam",
               loss="sparse_categorical_crossentropy",
               metrics=["accuracy"])

imagen = Image.open("numero.png").convert("L")
imagen = imagen.resize((28,28))
imagen_array = np.array(imagen)
imagen_array = imagen_array/255.0
imagen_array = np.expand_dims(imagen_array,axis=0)

modelo.fit(train_images,train_labels, epochs=5)

prediccion = modelo.predict(imagen_array)
resultado = np.argmax(prediccion)

plt.figure(figsize=(3,3))
plt.imshow(imagen_array[0],cmap="gray")
plt.title(f"Prediccion: {resultado}")
plt.axis("off")
plt.show()