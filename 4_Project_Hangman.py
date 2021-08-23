import random
import os
from Day_7_Hangman_Art import _etapas, _logo
from Day_7_Hangman_Words import _list_palabras

def clear(): os.system('cls') #on Windows System

print(f'{_logo}\n')
_juego_terminado = False
_vidas = len(_etapas) -1

_palabra_aleatoria = random.choice(_list_palabras)
_longitud_palabra = len(_palabra_aleatoria)

_visualizacion = []

for _ in range(_longitud_palabra):
    _visualizacion += "_"

print(f'{_visualizacion}\n')

while not _juego_terminado:

    _letra_escojida = input("Adivine una letra: ").lower()
    
    clear()

    if _letra_escojida in _visualizacion:
        print(f"Ya habias elegido la letra {_letra_escojida}")

    for _indice in range(_longitud_palabra):
        _letra = _palabra_aleatoria[_indice]
        if _letra == _letra_escojida:
            _visualizacion[_indice] = _letra
    
    print(f"{' '.join(_visualizacion)}")

    if _letra_escojida not in _palabra_aleatoria:
        print("Esa letra no esta en la palabra. Pierdes una vida")
        _vidas -= 1
        if _vidas == 0:
            _juego_terminado = True
            print("You Lose")

    if not "_" in _visualizacion:
        _juego_terminado = True
        print("You Win")

    print(_etapas[_vidas])
    
input()