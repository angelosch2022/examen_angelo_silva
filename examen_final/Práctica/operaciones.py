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
import random

def generar_lista_aleatoria(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError(f"***n={n} debe ser un entero positivo***")

    aleatorios= random.choices(range(1, 101), k=n)
    return aleatorios

def lista_sin_duplicados(lista):
    return list(set(lista))

def listas_ordenadas(lista):
    return sorted(lista), sorted(lista, reverse=True)

def mayor_numero_par(lista):
    pares=[x for x in lista if x%2==0]
    if not pares:
        return None
    return max(pares)

def elemento_en_posicion(lista, posicion):
    try:
        return lista[posicion]
    except IndexError:
        raise IndexError(f"***Posición {posicion} fuera del rango***")