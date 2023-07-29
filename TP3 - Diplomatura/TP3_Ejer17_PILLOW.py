# Implementar una funcióon que genere una versión en tonos sepia de una imagen pasada
# como argumento. Una posibilidad es utilizar los valores recomendados por Microsoft para
# generar un pixel sepia en base a un pixel RGB, dado por los siguientes valores.
# el nuevo rojo pasará a ser (R * .393) + (G * .769) + (B * .189)
# el nuevo verde será (R * .349) + (G * .686) + (B * .168)
# y el nuevo azul será (R * .272) + (G * .534) + (B * .131)

from PIL import Image as mg

def sepia(imagen):
    matriz = imagen.load()   
    for i in range(imagen.height):
        for j in range(imagen.width):
            R, G, B = imagen.getpixel((j, i))            
            r2 = int((R * .393) + (G * .769) + (B * .189)) #rojo
            r2 = 255 if r2 > 255 else r2

            g2 = int((R * .349) + (G * .686) + (B * .168)) #verde
            g2 = 255 if g2 > 255 else g2
            
            b2 = int((R * .272) + (G * .534) + (B * .131)) #azul
            b2 = 255 if b2 > 255 else b2

            matriz[j, i] = (r2, g2, b2)
            
    return imagen
