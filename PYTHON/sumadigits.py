def sumadigits():
    numero=input("Dime un numero de doz cifras: ")
    decenas=numero/10
    unidades=numero%10
    print "La suma de las cifras de ", numero, "es", decenas+unidades

sumadigits()
