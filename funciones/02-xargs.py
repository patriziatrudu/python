def suma(*numeros): # * ens diu que es iterale
    resultado=0
    for numero in numeros:
        resultado += numero
    print(resultado)
   
   
    
    
#per obtenir tots els arguments que volem cridar en una funcio
suma(5,8,7)
suma(5,8)
