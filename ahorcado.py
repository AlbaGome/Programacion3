import random

def jugar():
    print('================================')
    print('Bienvenido al Juego del Ahorcado')
    print('================================')

    archivo = open('palabras.txt','r')
    palabras = []
    for linea in archivo:
        linea = linea.strip()
        palabras.append(linea)
   
    archivo.close()
    numero = random.randrange(0,len(palabras))
    
    palabra_secreta = palabras[numero].lower()
    letras_acertadas =['_' for elemento in palabra_secreta]
    
    ahorcado = False
    acerto = False

    while(not ahorcado and not acerto):
        entrada = input ('ingrese una letra...')
        entrada = entrada.strip()       #elimina espacios en blanco a la izquierda y derecha
        entrada = entrada.lower()       #convierte a letras minusculas
        indice = 0 
        for letra in palabra_secreta:
            if(entrada==letra):
                letras_acertadas[indice]=letra
                #print('Se encontro la letra {} en la posicion {}'.format(letra, indice))
                
            indice = indice + 1
        print(letras_acertadas)

    print("Fin del Juego")
    
if(__name__=='__main__'):
    
    jugar()   