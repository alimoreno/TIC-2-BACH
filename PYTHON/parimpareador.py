def parimpareador():
    x=input("Dime un numero ")
    y=input("Dime otro numero ")
    if(x%2>0 and y%2>0):
        print "Los dos numeros son impares"
    if((x%2==0 and y%2>0) or (x%2>0 and y%2==0)):
        print "Un numero es par y el otro impar"
    if(x%2==0 and y%2==0):
        print "Los dos numeros son pares"
parimpareador()
