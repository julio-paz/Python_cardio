menu = """
Bienvenido al conversor de distancia  ´

1 - Millas a kilometros 
2 - kilometros a millas 

Elige una opcion: """

opcion = input(menu)

if opcion == '1':
    millas = input("ingresa cantidad de millas: ")
    millas = float(millas)
    valor_milla = 1.609344
    kilometros = millas * valor_milla
    kilometros = round(kilometros,2)
    kilometros = str(kilometros)
    print("tienes " + kilometros + "kilometros")
elif opcion == '2':
    kilometros = input("ingresa cantidad de kilometros: ")
    kilometros = float(kilometros)
    valor_kilometro = 0.6213
    millas = kilometros * valor_kilometro
    millas = round(millas,2)
    millas = str(millas)
    print("tienes " + millas + "millas")
else :
    print("Ingesa una opcion correcta por favor")
