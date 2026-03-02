========================================
        MODULO DE REGISTRO DE VENTAS
========================================

1. FUNCIONALIDAD DEL PROGRAMA
-----------------------------
Este programa permite registrar una venta individual, calcular los valores
asociados según reglas básicas del negocio y mostrar un resumen claro en
consola.  

El alcance está limitado a *una sola venta por ejecución*.

---

2. REQUERIMIENTOS FUNCIONALES
-----------------------------
El programa solicita al usuario:

- Nombre del cliente
- Precio unitario del producto
- Cantidad de productos comprados
- Confirmación de si el cliente tiene membresía VIP (Sí / No)

---

3. REGLAS DE NEGOCIO
--------------------
1. Subtotal = Precio Unitario × Cantidad
2. Si el cliente es VIP, se aplica un 10% de descuento:
   Descuento = Subtotal × 0.10
3. Total Final = Subtotal - Descuento

---

4. RESULTADO ESPERADO
---------------------
Al finalizar la ejecución, se muestra en consola:

--------------------------------
| Nombre del cliente: Juan Pérez
| Subtotal: $2000.00
| Descuento aplicado: $200.00
| Total final a pagar: $1800.00
--------------------------------

---

5. RESTRICCIONES TÉCNICAS
-------------------------
- Desarrollo en Python.
- Uso de:
  - Variables.
  - Tipos de datos básicos: int, float, str, bool.
  - Entrada de datos por consola (input()).
  - Salida de información por consola (print()).
- No se requiere persistencia de datos.

---

6. CRITERIOS DE ACEPTACIÓN
---------------------------
- Permite registrar una venta sin errores.
- Los cálculos son correctos según las reglas definidas.
- La información se muestra de forma clara y legible.
- Todos los campos obligatorios deben estar completos antes de calcular.

---

7. FLUJO DEL PROGRAMA
---------------------
1. Solicitar nombre del cliente.
2. Solicitar precio unitario del producto.
3. Solicitar cantidad de productos.
4. Preguntar si el cliente es VIP.
5. Validar que los datos estén completos y sean válidos.
6. Calcular subtotal.
7. Aplicar descuento si corresponde.
8. Calcular total final.
9. Mostrar resumen de la venta en consola.

---

8. EJEMPLOS DE USO
-------------------
Caso 1: Cliente Normal
- Cantidad: 2
- Precio: $500
- VIP: No

Resultado:
- Subtotal: $1000
- Descuento: $0
- Total: $1000

Caso 2: Cliente VIP
- Cantidad: 3
- Precio: $1000
- VIP: Sí

Resultado:
- Subtotal: $3000
- Descuento: $300
- Total: $2700

========================================
