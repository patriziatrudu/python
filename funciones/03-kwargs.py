def get_product(**datos): 
    print(datos["id"],datos["name"])
    
get_product(id="23",
            name="iphone",
            desc="este es un iphone")