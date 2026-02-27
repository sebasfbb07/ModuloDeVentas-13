def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def calcular_descuento(subtotal, porcentaje):
    return subtotal * (porcentaje / 100)

def calcular_total(subtotal, descuento):
    return subtotal - descuento