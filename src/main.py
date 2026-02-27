print("-"*80)
print("                               BIENVENIDO USUARIO!    :)")
print("-"*80)

from ventas import calculos, cliente
from interfaz import input_output as io

def main():
    
    nombre = io.pedir_nombre()
    precio = io.pedir_precio()
    cantidad = io.pedir_cantidad()
    respuesta_vip = io.pedir_respuesta_vip()

    subtotal = calculos.calcular_subtotal(precio, cantidad)
    es_cliente_vip = cliente.es_vip(respuesta_vip)
    descuento = calculos.calcular_descuento(subtotal, 10) if es_cliente_vip else 0
    total = calculos.calcular_total(subtotal, descuento)

    io.mostrar_resumen(nombre, subtotal, descuento, total)

if __name__ == "__main__":
    main()




