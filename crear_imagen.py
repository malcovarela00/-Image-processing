import cv2
import numpy as np
import matplotlib.pyplot as plt

## Crear una matriz de ceros de tamaño (3,5)
im = np.zeros((3,10), dtype=int)
## Mostrar la matriz
print(im) 
## Mostrar la imagen
plt.imshow(im)
plt.show()
