from funciones import crear_producto, crear_mesa, crear_cliente, crear_factura ,registro_venta
from funcion_examen import producto_mas_vendido
while True:
    print("---------------------------------------")
    print("SISTEMA DE FACRURACION RESTAURANTE ACME")
    print("1. Ver/agregar productos")
    print("2. Ver/agregar mesas")
    print("3. Ver/registar clientes")
    print("4. Crear factura")
    print("5. Registro de ventas")
    print("6. Ranking de productos")
    print("7. Salir")
    print("---------------------------------------")
    opcion = input("Digite la opcion: ")
    print("---------------------------------------")

    if opcion == "1":
        crear_producto()

    elif opcion == "2":
        crear_mesa()

    elif opcion == "3":
        crear_cliente()

    elif opcion == "4":
        crear_factura()

    elif opcion == "5":
        registro_venta()

    elif opcion == "6":
        producto_mas_vendido()

    elif opcion == "7":
        print("Saliendo del sistema...")
        break
    else:
        print("Opcion no valida")