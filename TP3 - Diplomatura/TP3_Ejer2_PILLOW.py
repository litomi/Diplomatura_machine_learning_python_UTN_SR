from PIL import Image as img
import numpy as np

imagen = img.open('imagenes\\cuadrado.jpg')

pixeles = np.array(imagen)

for i in range(len(pixeles)):
    for j in range(len(pixeles[i])):
        r, g, b = pixeles[i][j]
        if (0, 0, 0) == (r, g, b):
            pixeles[i][j] = (0, 255, 0)

imagen = img.fromarray(pixeles)

imagen.show()
