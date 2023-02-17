import numpy as np
import cv2
import matplotlib.pyplot as plt

## Leer la imagen
imagen = cv2.imread('img3.png')

## Funcion para mostrar la resolución de la imagen
def resolucion(imagen):
    return imagen.shape

## Definir una funcion para mostrar la imagen
def mostrar_imagen(imagen):
    plt.imshow(imagen)
    plt.show()
## Funcion para encontrar el color predominante de la imagen
def color_predominante(imagen):
    verde = 0
    azul = 0
    rojo = 0
    negro = 0
    for i in range(len(imagen)):
        for j in range(len( imagen[i])):
            if imagen[i][j][0] < 80 and imagen[i][j][1] > 100 and imagen[i][j][2] < 80:
                verde += 1
            elif imagen[i][j][0] < 80 and imagen[i][j][1] < 80 and imagen[i][j][2] > 100:
                azul += 1
            elif imagen[i][j][0] > 100 and imagen[i][j][1] < 80 and imagen[i][j][2] < 80:
                rojo += 1
            elif imagen[i][j][0] < 30 and imagen[i][j][1] < 30 and imagen[i][j][2] < 30:
                negro += 1
    print(verde, rojo, negro, azul)    
    if verde > azul and verde > rojo and verde > negro:
        print('El color Verde es el predominante')
    elif azul > verde and azul > rojo and azul > negro:
        print('El color Azul es el predominante')
    elif rojo > verde and rojo > azul and rojo > negro:
        print('El color Rojo es el predominante')
    elif negro > verde and negro > azul and negro > rojo:
        print('El color Negro es el predominante')
    else:
        print('No hay color predominante')

resolucion(imagen)
color_predominante(imagen)
mostrar_imagen(imagen)