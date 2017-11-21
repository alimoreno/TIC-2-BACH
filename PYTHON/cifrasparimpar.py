def cifrasparimpar():
    x=0
    n_cifras_pares=0
    n_cifras_impares=0
    numero=input("Dime un numero ")
    while(numero>0):
        x=numero%10
        if(x%2==0):
            n_cifras_pares=n_cifras_pares+1
        if(x%2>0):
            n_cifras_impares=n_cifras_impares+1
        numero=numero/10
    suma=n_cifras_pares+n_cifras_impares
    print "Hay", suma, "cifras en tu numero"
    print "Hay", n_cifras_pares, "cifras pares y", n_cifras_impares, "cifras impares"
cifrasparimpar()
