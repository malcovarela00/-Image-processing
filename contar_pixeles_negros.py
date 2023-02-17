import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread('img.png')
## Mostrar la resolución de la imagen
print(imagen.shape)

## Mostrar la matriz
print(imagen)

## Guardar los pixeles negros y contarlos
fila = []
columna = []
cont = 0
for i in range(len(imagen)):
    for j in range(len( imagen[i])):
        if imagen[i][j][0] == 0 and imagen[i][j][1] == 0 and imagen[i][j][2] == 0:
            cont += 1
            fila.append(i)
            columna.append(j)
print('hay', cont, 'pixeles negros')

for n in range(len(fila)):
    print('En la posición: ', fila[n], ',', columna[n])

## Mostrar la imagen
plt.imshow(imagen)
plt.show()