buscar=10

for numero in range(5): #secuencia de numeros
    print(numero)
    if numero==buscar:
        print("encontrado", buscar)
        break #detiene la ejecucion del codigo
else:
    print("no encontre el numero buscado :( ")
    
    
for char in "Ultimate python":
    print (char)