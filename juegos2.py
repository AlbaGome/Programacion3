import ahorcado 
import adivinanza

print('========================================')
print('Elija su juego')
print('========================================')

print ('(1) ahorcado (2) adivinanza')
juego = int(input('cual juego?'))

if(juego ==1):
    print('Juego ahorcado')
    ahorcado.jugar_ahorcado()
elif(juego ==2):
    print('Juego adivinaza')
    adivinanza.jugar_adivinanza()