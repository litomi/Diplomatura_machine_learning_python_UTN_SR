# 12. Implementar una función llamada hamming pal, que calcule la distancia de Hamming
# entre dos palabras o cadenas de caracteres, de igual longitud.

def hamming_pal(txt_1, txt_2):   
    n = 0 
    if len(txt_1) != len(txt_2):
        n = -1
    else:
        for i in range(len(txt_1)):
            if txt_1[i] != txt_2[i]:
                n += 1
    return n
