"""
2. Procesamiento de números mediante módulos (3 puntos)
Desarrollar un programa que procese números enteros utilizando funciones definidas en un módulo independiente.
Requisitos:
    • Crear operaciones.py con una función que genere una lista de n números enteros aleatorios entre 1 y 100;
    validar mediante excepciones que n sea entero positivo.
    • Implementar una función que retorne la lista sin elementos repetidos.
    • Crear una función que retorne dos listas independientes: una ascendente y otra descendente.
    • Implementar una función que retorne el mayor número par; si no existe, comunicarlo.
    • Crear una función que reciba una lista y una posición, retorne el elemento correspondiente y controle posiciones
    inexistentes mediante excepciones.
    • Crear main.py para llamar las funciones y mostrar sus resultados.
    Pruebas obligatorias:
    • Realizar dos ejecuciones con cantidades distintas; mostrar lista original, lista sin duplicados, ordenamientos y
    mayor par.
    • Probar una posición válida, otra fuera del rango y una cantidad n inválida.
"""
from operaciones import generar_lista_aleatoria, lista_sin_duplicados, listas_ordenadas, mayor_numero_par, elemento_en_posicion

#
def operacion(n,posicion):
    try:
        lista= generar_lista_aleatoria(n)
        print(f"Lista original: {lista}")

        lista_sin_dup= lista_sin_duplicados(lista)
        print(f"Lista sin duplicados: {lista_sin_dup}")

        asc, desc= listas_ordenadas(lista)
        print(f"Lista ascendente: {asc}")
        print(f"Lista descendente: {desc}")

        mayor_par= mayor_numero_par(lista)
        if mayor_par is not None:
            print(f"Mayor número par: {mayor_par}")
        else:
            print("No existe un número par en la lista")

        try:
            elem= elemento_en_posicion(lista, posicion)
            print(f"Elemento en posición {posicion} es: {elem}")
        except IndexError as e:
            print(e)

    except ValueError as e:
        print(e)

# Ejecuciones de prueba
operacion(20, 2)  # válida
operacion(5, 10) # fuera del rango
operacion(-3, 0) # inválida

