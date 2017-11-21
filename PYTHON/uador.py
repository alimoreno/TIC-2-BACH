def pig_latin():
    texto=raw_input("Inserte el texto que quiere que sea uado: ")
    for cont in range (0,len(texto),1):
        if texto[cont]=="a" or texto[cont]=="A" or texto[cont]=="e" or texto[cont]=="E" or texto[cont]=="i" or texto[cont]=="I" or texto[cont]=="o" or texto[cont]=="O":
            print "u",
        else:
            print texto[cont],
  
pig_latin()
