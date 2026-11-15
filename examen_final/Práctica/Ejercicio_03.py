"""
3. Sistema de registro de pedidos de Rappi (3 puntos)
La empresa Rappi necesita registrar pedidos de delivery, calcular sus importes y controlar la fecha y hora de las
operaciones.
Requisitos:
    • Crear un decorador registrar_pedido que muestre fecha y hora de ejecución (horas, minutos y segundos) y un
    mensaje al finalizar correctamente.
    • Crear calcular_total, que reciba precios mediante *args y retorne su suma.
    • Crear procesar_pedido, que reciba el nombre del cliente y los precios de productos mediante **kwargs,
    retornando el importe total.
    • Validar que los precios sean numéricos y mayores que cero; ante un precio inválido, mostrar un mensaje y evitar
    el cálculo.
    • Aplicar el decorador a ambas funciones y mostrar los resultados junto con la fecha y hora
"""
from datetime import datetime

def registrar_pedido(func):
    def wrapper(*args, **kwargs):
        ahora = datetime.now()
        print(f"Fecha y hora de ejecución: {ahora.strftime('%H:%M:%S')}")
        resultado = func(*args, **kwargs)
        if resultado is not None:
            print("Pedido registrado correctamente")
        return resultado
    return wrapper

@registrar_pedido
def calcular_total(*args):
    total = 0
    for precio in args:
        if (
            isinstance(precio, bool)
            or not isinstance(precio, (int, float))
            or not precio > 0
        ):
            print(f"***Precio inválido: {precio}***")
            return None
        total += precio
    return total

@registrar_pedido
def procesar_pedido(cliente, **kwargs):
    precios = list(kwargs.values())
    total = calcular_total(*precios)
    if total is not None:
        print(f"Cliente: {cliente}")
        print(f"Importe total: {total}")
    else:
        print("No se pudo procesar el pedido debido a precios inválidos")
    return total

# Ejecuciones de prueba
procesar_pedido("Juan", producto1=10, producto2="op")
print("*"*30)
procesar_pedido("Ana", producto1=15, producto2=-5)  #invalido
print("*"*30)
procesar_pedido("Luis", producto1=30, producto2=25)
print("*"*30)
procesar_pedido("Marta", producto1=0, producto2=50)  #invalido
