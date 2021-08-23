"""

"""

import random

_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
_numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
_simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#_letras = 52
#_numero = 10
#simbolos = 9

print("Bienvenido al Generador de Password")
_entrada_letras = int(input('Cuantas letras deseas que tenga tu password: '))
_entrada_simbolos = int(input('Cuantos simbolos desea que tenga tu password: '))
_entrada_numeros = int(input('Cuantos numeros desea que tenga tu password: '))

#Easy Version
_password = ""

#for i in range(_entrada_letras):
    #_password += random.choice(_letras)

#for i in range(_entrada_simbolos):
    #_password += random.choice(_simbolos)

#for i in range(_entrada_numeros):
    #_password += random.choice(_numeros)

#print(f'Tu contraseña es: {_password}')

#Hard Version
_list_password = []

for i in range(_entrada_letras):
    _list_password += random.choice(_letras)

for i in range(_entrada_simbolos):
    _list_password += random.choice(_simbolos)

for i in range(_entrada_numeros):
    _list_password += random.choice(_numeros)

random.shuffle(_list_password)

_password_aleatorio = ""

for i in _list_password:
    _password_aleatorio += i

print(f'Tu contraseña es: {_password_aleatorio}')
input()