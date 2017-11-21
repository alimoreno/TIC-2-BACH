def eiuador():
    texto=raw_input("Inserte el texto para ser eiuado: ")
    lista1=list(texto)
    for cont in range (0,len(texto),1):
        if texto[cont]=="a":
            lista1[cont]="u"
        if texto[cont]=="e":
            lista1[cont]="u"
        if texto[cont]=="i":
            lista1[cont]="u"
        if texto[cont]=="o":
            lista1[cont]="u"
    string="".join(lista1)
    print string
eiuador()
