# 13. Implementar la funciÓn distancia de hamming, pero para imágenes. Se llamaría hamming
# y tomaría dos imagenes como parámetros.

def hamming(img1, img2):   
    n = 0 
    if len(img1) != len(img1):
        n = -1
    else:
        for i in range(len(img1)):
            if img1[i] != img2[i]:
                n += 1
    return n
