def esprimo(cont):
    respuesta=1
    for cont2 in range(cont-1,1,-1):
        if(cont%cont2==0):
          respuesta=0
    return(respuesta)

def factorizacion():
    numero=input("Dime un numero")
    while(numero>0):
        for cont in range(2,numero,1):
         if esprimo(cont)==1:
             if(numero%cont==0):
                 print cont,
                 numero=numero/cont
factorizacion()

    
   
