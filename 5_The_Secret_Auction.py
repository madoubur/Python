#from Day_9_The_Secret_Auction_Art import logo

#print(logo)

flag = True
_ofertantes = {}
_mayor = 0
_name = ""
while flag:
    _name = input("Ingrese su nombre: ")
    _oferta = input("Ingresa tu oferta: ")
    _ofertantes[_name] = _oferta

     _opcion = input("Hay otros ofertante (si) o (no): ")

    if _opcion == "no":
        flag = False
else:
    for key in _ofertantes:
        if int(_ofertantes[key]) > _mayor:
            _mayor = int(_ofertantes[key])
            _name = key

    print(f"La oferta mayor la hizo {_name} con el valor de {_mayor}")
    print("Fin del Programa")
    input()