menu = """
Bienvenido al calculo de volumenes , seleccione en volumen a calcular 

1 - cubo
2 - piramide cuadrangular 

Elige una opcion: """

opcion = input(menu)

if opcion == '1':
    lado = input("ingresa medida del lado: ")
    lado = float(lado)
    volumen_cubo = lado * lado * lado
    volumen_cubo = round(volumen_cubo,2)
    volumen_cubo = str(volumen_cubo)
    print("el volumen del cubo es de " + volumen_cubo + " unidades de volumen ")
elif opcion == '2':
    base = input("ingresa medida de la base : ")
    base = float(base)
    altura = input("ingresa la altura : ")
    altura = float(altura)
    volumen_piramide = (((base*base)*altura)/3)
    volumen_piramide = round(volumen_piramide,2)
    volumen_piramide = str(volumen_piramide)
    print("el volumen del la piramode es de " + volumen_piramide + " unidades de volumen ")
else :
    print("Ingesa una opcion correcta por favor")
