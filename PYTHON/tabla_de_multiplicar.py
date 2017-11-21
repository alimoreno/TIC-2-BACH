def tabla_de_multiplicar():
    numero=input("Dime de que numero deseas la tabla")
    for cont in range(1,11,1):
        print numero,"x", cont, "=", numero*cont
tabla_de_multiplicar()
