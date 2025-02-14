def hola(nombre,apellido="feliz"):  #parametros
    print("hola mundo")
    print(f"bienvenida {nombre} {apellido}")
    
    
hola("Patrizia","trudu")  #arguemntos
hola("chanchito")



#si volem mostrar els arguments del reves, li hem de dir quin es l'argument 
hola(apellido="trudu",nombre="patrizia")