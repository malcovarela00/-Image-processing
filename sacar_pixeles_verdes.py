import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread('img.png')
## Mostrar la resolución de la imagen
print(imagen.shape)

## Mostrar la imagen
plt.imshow(imagen)
plt.show()

## Mostrar la matriz
print(imagen)

## Eliminar los pixeles verdes de la matriz
for i in range(len(imagen)):
    for j in range(len( imagen[i])):
        if imagen[i][j][0] == 76 and imagen[i][j][1] == 177 and imagen[i][j][2] == 34:
            imagen[i][j] = [255, 255, 255]

## Mostrar la imagen
plt.imshow(imagen)
plt.show()

## Cambiar el color negro por rojo de la imagen
for i in range(len(imagen)):
    for j in range(len( imagen[i])):
        if imagen[i][j][0] == 0 and imagen[i][j][1] == 0 and imagen[i][j][2] == 0:
            imagen[i][j] = [255, 0, 0]

## Mostrar la imagen
plt.imshow(imagen)
plt.show()

