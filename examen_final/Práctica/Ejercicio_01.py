"""
1. Sistema de alquiler de vehículos (3 puntos)
Una empresa de alquiler de vehículos necesita registrar sus unidades, administrar tarifas y calcular descuentos
según los días de alquiler.
Requisitos:
    • Crear una clase Vehiculo con marca, modelo y anio=2020; incluir métodos para actualizar marca y año (mayor
    que cero) y mostrar sus datos.
    • Crear VehiculoAlquiler, que herede de Vehiculo y agregue codigo y tarifa_diaria.
    • Encapsular tarifa_diaria; permitir su actualización solo mediante un método que valide valores mayores que
    cero.
    • Implementar aumentar_tarifa(porcentaje=10) para incrementar la tarifa diaria.
    • Implementar calcular_descuento(dias_alquiler) sobre el importe total: menos de 2 días (5 %), de 2 a 5 días (10
    %) y más de 5 días (15 %).
    • Mostrar los datos del vehículo, su tarifa actual, el importe antes del descuento y el total final.
Pruebas obligatorias:
    • Crear dos vehículos diferentes y aplicar dos incrementos consecutivos a la tarifa de uno de ellos.
    • Calcular descuentos e importes finales con distintas cantidades de días.
    • Intentar asignar una tarifa negativa, verificar que no se modifique y mostrar los resultados.
"""

class Vehiculo:
    def __init__(self, marca,modelo,anio=2020):
        self.marca=marca
        self.modelo=modelo
        self.anio=anio

    def actualizar_marca(self, nueva_marca):
        self.marca = nueva_marca

    def actualizar_anio(self,nuevo_anio):
        if nuevo_anio > 0:
            self.anio = nuevo_anio

    def mostrar_datos(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Año: {self.anio}")

#
class VehiculoAlquiler(Vehiculo):
    def __init__(self, marca, modelo, anio=2020, codigo=None, tarifa_diaria=0):
        super().__init__(marca, modelo, anio)
        self.codigo = codigo
        self.__tarifa_diaria = tarifa_diaria

    def actualizar_tarifa(self, nueva_tarifa):
        if not self.validar_tarifa_diaria(nueva_tarifa):
            return
        self.__tarifa_diaria = nueva_tarifa

    def aumentar_tarifa(self, porcentaje=10):
        self.__tarifa_diaria += self.__tarifa_diaria * (porcentaje / 100)

    def calcular_descuento(self, dias_alquiler):
        importe_total = self.__tarifa_diaria * dias_alquiler
        if dias_alquiler<2:
            descuento = 0.05
        elif 2 <= dias_alquiler <= 5:
            descuento = 0.10
        else:
            descuento = 0.15
        total_final=importe_total*(1 - descuento)
        return importe_total, total_final

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Codigo: {self.codigo} | Tarifa diaria: {self.__tarifa_diaria}")
        print(f"Importe antes del descuento: {self.calcular_descuento(1)[0]:.2f}")
        print(f"Total final con descuento: {self.calcular_descuento(1)[1]:.2f}")

    #validaciones
    def validar_tarifa_diaria(self, tarifa):
        if tarifa <= 0:
            print(f"************La tarifa diaria de {tarifa} no es valida****************")
            return False
        return True

vehiculo1 = VehiculoAlquiler("Toyota", "Corolla", 2022, "A001", 100)
vehiculo2 = VehiculoAlquiler("Honda", "Civic", 2021, "B002", 120)
#aumentos
vehiculo1.aumentar_tarifa(porcentaje=10)
vehiculo1.aumentar_tarifa(porcentaje=10)

#descuentos
vehiculo1.calcular_descuento(1)
vehiculo1.calcular_descuento(3)
vehiculo1.calcular_descuento(6)

vehiculo2.calcular_descuento(1)
vehiculo2.calcular_descuento(3)
vehiculo2.calcular_descuento(6)

vehiculo1.actualizar_tarifa(-100) #actualizar tarifa negativa

vehiculo1.mostrar_datos()
print("*"*30)
vehiculo2.mostrar_datos()
