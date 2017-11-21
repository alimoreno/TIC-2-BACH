def reordenador():
    numero=input ("Dime un numero de tres cifras: ")
    unidades=numero%10
    numero=numero/10
    decenas=numero%10
    numero=numero/10
    centenas=numero%10
    numero=numero/10
    print "El nuevo orden es: ", unidades, decenas, centenas
reordenador()

def reordenador_1():
    numero=input ("Dime un numero: ")
    print "El nuevo orden es: "
    while(numero>0):
        x=numero%10
        numero=numero/10
        list.append(x)
    return x

reordenador_1()
