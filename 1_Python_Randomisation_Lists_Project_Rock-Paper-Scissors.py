import random

_piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

_papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

_tijera = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

_imagenes = [_piedra, _papel, _tijera]

_opcion_usuario = int(input('Escoje una opcion: 0 para Piedra, 1 para Papel o 2 para Tijera: '))
print(_imagenes[_opcion_usuario])

_opcion_cpu = random.randint(0,2)
print('CPU eligio: ')
print(_imagenes[_opcion_cpu])

if _opcion_usuario >= 3 or _opcion_usuario < 0:
    print('Ingreso un numero invalido, Perdiste!')
elif _opcion_usuario == 0 and _opcion_cpu == 2:
    print('You Win')
elif _opcion_cpu == 0 and _opcion_usuario == 2:
    print('You Lose')
elif _opcion_cpu > _opcion_usuario:
    print('You Lose')
elif _opcion_usuario > _opcion_cpu:
    print('You Win')
elif _opcion_cpu == _opcion_usuario:
    print("It's a draw")
input()





