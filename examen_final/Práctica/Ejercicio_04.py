"""
4. Control de inventario mediante diccionarios (2 puntos)
Una tienda requiere administrar productos disponibles y registrar operaciones de compra.
Requisitos:
    • Crear un diccionario con al menos cuatro productos; cada producto debe registrar nombre, precio y cantidad
    disponible.
    • Implementar una función que muestre todos los productos y sus datos.
    • Crear una función que reciba un producto y la cantidad solicitada, valide su existencia y disponibilidad, calcule
    el importe y actualice las existencias cuando la compra sea válida.
    • Implementar una función que retorne el valor monetario total del inventario.
    Pruebas obligatorias:
    • Mostrar el inventario inicial; realizar una compra válida, otra de un producto inexistente y otra con cantidad
    superior al stock.
    • Mostrar el inventario actualizado y su valor monetario total.
"""
#productos de computo
productos={
    "laptop": {"nombre": "Laptop", "precio": 1500, "cantidad": 10},
    "mouse": {"nombre": "Mouse", "precio": 50, "cantidad": 50},
    "teclado": {"nombre": "Teclado", "precio": 100, "cantidad": 30},
    "monitor": {"nombre": "Monitor", "precio": 300, "cantidad": 20}
}

def mostrar_productos():
    print("Inventario:")
    for clave, producto in productos.items():
        print(f"- {producto['nombre']}: Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")    
    print()

def comprar(producto, cant_comprar):
    if producto not in productos:
        print(f"***Producto inexistente: {producto}***")
        return None
    if cant_comprar <= 0:
        print(f"***Cantidad inválida: {cant_comprar}***")
        return None
    if productos[producto]["cantidad"] < cant_comprar:
        print(f"***Cantidad solicitada {cant_comprar} superior al stock: {productos[producto]['cantidad']}***")
        return None
    
    importe = productos[producto]["precio"] * cant_comprar
    productos[producto]["cantidad"] -= cant_comprar
    print(f"Compra realizada: {producto}, Cantidad: {cant_comprar}, Importe: {importe:.2f}")
    return importe

def valor_total_inventario():
    total = 0
    for producto in productos.values():
        total += producto["precio"] * producto["cantidad"]
    return total

#pruebas
mostrar_productos()
comprar("laptop", 2)  # validaa
comprar("tablet", 1)  # no existe producto
comprar("mouse", 100)  # cantidad superior al stock
mostrar_productos() #con los cambios
print(f"Valor total del inventario S/ : {valor_total_inventario():.2f}")
