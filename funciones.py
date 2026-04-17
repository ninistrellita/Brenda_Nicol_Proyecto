import csv

from datetime import datetime
from funcion_examen import venta_producto

def buscar_por_codigo(archivo, codigo_buscado):
    with open(archivo, "r", newline="") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            if int(fila["codigo"]) == codigo_buscado:
                return fila
    return None

def crear_factura():

    print("---------- CREAR FACTURA ----------")

    cod_mesa = int(input("Ingrese codigo de la mesa: "))
    mesa = buscar_por_codigo("BRENDA_NICOL_PROYECTO/Mesas.csv", cod_mesa)
    if mesa is None:
        print("La mesa no se encuentra registrada")
        return

    cod_cliente = int(input("Ingrese codigo del cliente: "))
    cliente = buscar_por_codigo("BRENDA_NICOL_PROYECTO/Clientes.csv", cod_cliente)
    if cliente is None:
        print("El cliente no se encuentra registrado")
        return

    detalles = []
    total = 0
    total_productos = 0
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    while True:
        cod_producto = int(input("Ingrese codigo del producto: "))
        producto = buscar_por_codigo("BRENDA_NICOL_PROYECTO/Producto.csv", cod_producto)

        if producto is None:
            print("El producto no se encuentra registrado")
        else:
            cantidad = int(input("Ingrese la cantidad: "))
            valor = int(producto["valor"])

            valor_iva = valor * 0.19
            precio_con_iva = valor + valor_iva
            subtotal = precio_con_iva * cantidad

            detalles.append({
                "codigo": producto["codigo"],
                "nombre": producto["nombre"],
                "cantidad": cantidad,
                "valor_unitario": valor,
                "iva": valor_iva,
                "subtotal": subtotal
            })


            total += subtotal
            total_productos += cantidad
        seguir = input("Desea agregar otro producto? (si/no): ").lower()
        if seguir == "si":
            continue
        elif seguir == "no":
            break
        else:
            print("Opcion no valida")

    print("-----------FACTURA----------")
    print("Fecha:", fecha)
    print("Mesa:", mesa["nombre"])
    print("Cliente:", cliente["nombre"])
    print("Telefono:", cliente["telefono"])
    print("Correo:", cliente["correo"])
    print("--------------------------------")

    for item in detalles:
        print(
            f"Cod: {item['codigo']} | "
            f"Producto: {item['nombre']} | "
            f"Cantidad: {item['cantidad']} | "
            f"Valor unitario: {item['valor_unitario']} | "
            f"IVA: {item['iva']}% | "
            f"Subtotal: {item['subtotal']}"
        )

    print("--------------------------------")
    print("Total productos:", total_productos)
    print("TOTAL A PAGAR:", total)

    guardar = input("Desea guardar la factura? (si/no): ").lower()
    if guardar == "si":
        nombre_archivo = ("BRENDA_NICOL_PROYECTO/factura.csv")
        with open(nombre_archivo, "a") as f:
            f.write(f"-----------FACTURA----------\nFecha: {fecha}\nMesa: {mesa['nombre']}\nCliente: {cliente['nombre']}\nTelefono: {cliente['telefono']}\nCorreo: {cliente['correo']}\n--------------------------------\n")

            for item in detalles:
                f.write(
                    f"Cod: {item['codigo']} |"
                    f"Producto: {item['nombre']} \n| "
                    f"Cantidad: {item['cantidad']} \n| "
                    f"Valor unitario: {item['valor_unitario']}\n | "
                    f"IVA: {item['iva']}% |\n "
                    f"Subtotal: {item['subtotal']}\n"
                )

            f.write("\n--------------------------------\n")
            f.write(f"Total productos: {total_productos}\n")
            f.write(f"TOTAL A PAGAR: {total}\n")

        guardar_venta(fecha, mesa["nombre"], cliente["nombre"], total)

        for item in detalles :
            venta_producto(producto["nombre"], cantidad , fecha)

        print("Factura guardada correctamente")
    elif guardar == "no":
        print("Factura no guardada")
    else:
        print("Opcion no valida")


def guardar_venta(fecha, nombre_mesa, nombre_cliente, total_pagar):
    encabezado = ["fecha", "mesa", "cliente", "total"]

    try:
        with open("BRENDA_NICOL_PROYECTO/ventas.csv", "r") as f:
            archivo_existe = True
    except FileNotFoundError:
        archivo_existe = False

    with open("ventas.csv", "a") as f:
        escribir = csv.DictWriter(f, fieldnames=encabezado)
        if not archivo_existe:
            escribir.writeheader()

        escribir.writerow({
            "fecha": fecha,
            "mesa": nombre_mesa,
            "cliente": nombre_cliente,
            "total": total_pagar
        })

def registro_venta():
    with open("BRENDA_NICOL_PROYECTO/ventas.csv", "r") as f:
        lector = csv.DictReader(f)
        for venta in lector:
            print(f"Fecha: {venta['fecha']} | Mesa: {venta['mesa']} | Cliente: {venta['cliente']} | Total: {venta['total']}")


def crear_producto():
    print("1. Agregar producto")
    print("2. Ver productos")
    print("---------------------------------------")
    opcion1 = input("Digite opcion: ")
    if opcion1 == "1":

        encabezado = ["codigo","nombre","valor","IVA"]
        codigo = int(input("Ingrese codigo: "))
        nombre = str(input("Ingrese nombre: "))
        valor = int(input("Ingrese valor: "))

        datos_productos = []
        productos = {}
        productos["codigo"] = codigo
        productos["nombre"] = nombre
        productos["valor"] = valor
        datos_productos.append(productos)

        try:
            with open("BRENDA_NICOL_PROYECTO/Producto.csv", "r") as f:
                archivo_existe = True
        except FileNotFoundError:
            archivo_existe = False

        with open("BRENDA_NICOL_PROYECTO/Producto.csv","a") as f:
            producto = csv.DictWriter(f,fieldnames = encabezado)
            if not archivo_existe:
                producto.writeheader()
            producto.writerows(datos_productos)

    if opcion1 == "2":
        with open("BRENDA_NICOL_PROYECTO/Producto.csv","r") as f:
            lector = csv.DictReader(f)
            for producto in lector:
                    print(producto["codigo"],"-",producto["nombre"])
    else:
        print("Opcion no valida")
def crear_mesa():
    print("1. Agregar mesas")
    print("2. Ver mesas")
    print("---------------------------------------")
    opcion2 = input("Digite opcion: ")

    if opcion2 == "1":

        encabezado = ["codigo","nombre","puestos"]
        codigo = int(input("Ingrese codigo: "))
        nombre = str(input("Ingrese nombre: "))
        puestos = int(input("Ingrese cantidad de puestos: "))

        datos_mesas = []
        mesas = {}
        mesas["codigo"]= codigo
        mesas["nombre"]= nombre
        mesas["puestos"]= puestos
        datos_mesas.append(mesas)

        try:
            with open("BRENDA_NICOL_PROYECTO/Mesas.csv", "r") as f:
                archivo_existe = True
        except FileNotFoundError:
            archivo_existe = False

        with open("BRENDA_NICOL_PROYECTO/Mesas.csv","a") as f:
            mesa = csv.DictWriter(f,fieldnames = encabezado)
            if not archivo_existe:
                mesa.writeheader()
            mesa.writerows(datos_mesas)

    elif opcion2 == "2":
        with open("BRENDA_NICOL_PROYECTO/Mesas.csv","r") as f:
            lector = csv.DictReader(f)
            for mesa in lector:
                print(mesa["codigo"],"-",mesa["nombre"])
    else:
        print("Opcion no valida")

def crear_cliente():
    print("1: Agregar cliente")
    print("2: Ver clientes")
    print("---------------------------------------")
    opcion3 = input("Digite opcion: ")

    if opcion3 == "1":

        encabezado = ["codigo","nombre","telefono","correo"]
        codigo = int(input("Ingrese codigo: "))
        nombre = str(input("Ingrese nombre: "))
        telefono = int(input("Ingrese telefono: "))
        correo = str(input("Ingrese correo: "))

        datos_clientes = []
        clientes = {}
        clientes["codigo"]= codigo
        clientes["nombre"]= nombre
        clientes["telefono"]= telefono
        clientes["correo"]= correo
        datos_clientes.append(clientes)

        try:
            with open("BRENDA_NICOL_PROYECTO/Clientes.csv", "r") as f:
                archivo_existe = True
        except FileNotFoundError:
            archivo_existe = False

        with open("BRENDA_NICOL_PROYECTO/Clientes.csv","a") as f:
            cliente = csv.DictWriter(f,fieldnames = encabezado)
            if not archivo_existe:
                cliente.writeheader()
            cliente.writerows(datos_clientes)

    elif opcion3 == "2":
        with open("BRENDA_NICOL_PROYECTO/Clientes.csv","r") as f:
            lector = csv.DictReader(f)
            for cliente in lector:
                print(cliente["codigo"],"-",cliente["nombre"],"-",cliente["telefono"],"-",cliente["correo"])
    else:
        print("Opcion no valida")

                
                
