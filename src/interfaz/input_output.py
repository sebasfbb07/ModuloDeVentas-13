def pedir_nombre():
    return input("Por favor ingrese el nombre del cliente: ")

def pedir_precio():
    while True:
        try:
            precio=int(input("Por favor ingrese el precio unitario del producto."))
            return precio
        except ValueError:
            print("Por favor ingrese un número.")
            

def pedir_cantidad():
     while True:
        try:
            cantidad=int(input("Por favor ingrese la cantidad de productos."))
            return cantidad
        except ValueError:
            print("Por favor ingrese un número.")

def pedir_respuesta_vip():
    return input("El cliente es VIP? (si/no): ")

def mostrar_resumen(nombre, subtotal, descuento, total):
    print("\n--- RESUMEN DE LA VENTA ---")
    print("Cliente:", nombre)
    print("Subtotal:", subtotal)
    print("Descuento aplicado:", descuento)
    print("Total a pagar:", total)