    import ahorcado
    import adivinanza
    print('========================================')
    print('Elija su juego')
    print('========================================')
    print ("(1)Horca  (2)Adivinanza")

    juego= int (input("¿Cual juego?"))

    if(juego==1):
        print("jugando horca")
    elif(juego==2):
        print ("jugando adivinanza")
        jugar_adivinanza()
