def jugar():
    print('================================')
    print('Bienvenido al Juego del Ahorcado')
    print('================================')

    palabra_secreta='mandarina'
    letras_acertadas=['','','','','','','','','_',]

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