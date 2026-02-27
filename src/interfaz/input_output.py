def pedir_nombre():
    return input("Por favor ingrese el nombre del cliente: ")

def pedir_precio():
    return float(input("Ingrese el valor unitario del producto: "))

def pedir_cantidad():
    return int(input("Ingrese la cantidad de productos: "))

def pedir_respuesta_vip():
    return input("El cliente es VIP? (si/no): ")

def mostrar_resumen(nombre, subtotal, descuento, total):
    print("\n--- RESUMEN DE LA VENTA ---")
    print("Cliente:", nombre)
    print("Subtotal:", subtotal)
    print("Descuento aplicado:", descuento)
    print("Total a pagar:", total)