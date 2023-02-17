import cv2
import numpy as np
import matplotlib.pyplot as plt
## Lectura de la imagen
im = cv2.imread('img.png')
## Mostrar la resolución de la imagen
print(im.shape)
## Mostrar la imagen
plt.imshow(im)
plt.show()
## Mostrar la imagen en escala de grises
plt.imshow(im, cmap='gray')
plt.show()
## Mostrar la imagen en escala de grises con histograma
plt.hist(im.ravel(),256,[0,256])
plt.show()
## Mostrar la imagen en escala de grises con histograma y color
plt.hist(im.ravel(),256,[0,256], color='r')
plt.show()

