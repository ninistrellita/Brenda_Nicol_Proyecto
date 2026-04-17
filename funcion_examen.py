import csv

def venta_producto (producto, cantidad, fecha , codigo):
    encabezado = ["Fecha" , "Codigo" , "Producto" , "Cantidad"]

    try:
        with open("BRENDA_NICOL_PROYECTO/venta_productos.csv" , "r") :
            encabezado_existe = True
    except FileNotFoundError :
        encabezado_existe = False

    with open ("BRENDA_NICOL_PROYECTO/venta_productos.csv" , "a") as f :
        escritor = csv.DictWriter(f,fieldnames=encabezado)
        if not encabezado_existe :
            escritor.writeheader()
            
        escritor.writerow({
            "Fecha" : fecha,
            "Codigo" : codigo,
            "Producto" : producto,
            "Cantidad" : cantidad

        })

def producto_mas_vendido(producto,cantidad) :
    
    with open ("venta_productos.csv" , "r") as f :
        lector = csv.DictReader(f)
        if producto > cantidad in lector :
            print(["Producto"] , ["Cantidad"])

        #conteo_productos = []
        #conteo = {}
        #producto ["Fecha"] = fecha
        #producto ["Codigo"] = codigo
        #producto ["Producto"] = producto
        #producto ["Cantidad"] = cantidad
        #conteo_productos.append(conteo)


    #fecha_inicio = (input("Digite la fecha inicial: "))
    #fecha_fin = (input("Digite la fecha final: "))
    
    #with open ("venta_productos.csv" , "r") as f:
        #lector = csv.DictReader (f)
        #for fecha_inicio in lector :
            #print(fecha_inicio["Codigo"], "-" , fecha_inicio["Producto"], "-" , fecha_inicio["Cantidad"])
        #for fecha_fin in lector :
         #   print(fecha_fin["Codigo"], "-" , fecha_fin["Producto"], "-" , fecha_fin["Cantidad"])
                


    

        


        
            







                
