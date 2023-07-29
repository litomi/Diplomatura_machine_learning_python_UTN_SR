# 9. Pedir una imagen al usuario y generar una nueva imagen que agregue un padding de 50px
# todo alrededor, del color que el usuario desee. Luego, generalizar en una función llamada
# padding que tome como parámetros una imagen y un valor de pixeles, y genere una nueva
# imagen que conste de la original más un borde de dicho grosor de pixeles todo alrededor.

from PIL import Image as mg
import numpy as np

#---------------------------------------------
#colores
colores = (
    (255, 255, 255), #blanco
    (0, 0, 0), #negro
    (0, 0, 255), #azul
    (255, 0, 0), #rojo
    (255, 255, 0), #amarillo
    (0, 128, 0), #verde
    (255, 165, 0), #naranja
    (75, 0, 130) #índigo
)

#-----------------------------------------------------
def menu_colores():
    print("Colores: ");
    print("1.- blanco")
    print("2.- negro")
    print("3.- azul")
    print("4.- rojo")
    print("5.- amarillo")
    print("6.- verde")
    print("7.- naranja")
    print("8.- índigo")
#-----------------------------------------------
def ingreso(min, max):
    while True:
        try:
            n = int(input(": "))
            if n < min or n > max:
                raise exception
            return n
        except:
            print("Sólo número entre {} y {}".format(min, max))


#----------------------------------------------

def padding_pillow(imagen, borde, color):

    ancho, alto = imagen.width, imagen.height    

    nueva_imagen = mg.new("RGB", (ancho + (borde * 2), alto + (borde * 2)), color)

    matriz = np.array(nueva_imagen)

    for i in range(alto):
        for j in range(ancho):
            matriz[i + borde, j + borde] = imagen.getpixel((j, i))

    return mg.fromarray(matriz)
    
#-----------------------------------------------------------------------

camino = "imagenes\\" + input("Ingrese nombre de la imagen (*.ext): ")

imagen = mg.open(camino)

if imagen is not None:
    print("Seleccionar un color:")
    menu_colores()
    color = ingreso(1, 8)

    print("Ingrese tamaño del borde en pixeles(0 - 100):", end=" ")
    pixeles = ingreso(0, 100)

    padding_pillow(imagen, pixeles, colores[color - 1]).show()
    
else:
    print("No se pudo abrir la imagen.")


    








