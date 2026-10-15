# ===============================================================
# Archivo: ejercisio_#1_.py
# Curso: SOFT-01 Principios de Programacion 1 - Seccion SCP0
# Integrantes: Isaac Peña Brenes, 
# Fecha 18/10/2026
# Descripción: Calcula los recursos necesarios para una misión.
#================================================================

# --- Entrada de datos ---
mision = input("Nombre de la misión: ")
tripulantes = int(input("Cantidad de tripulantes: "))
dias = int(input("Cantidad de días estimados para llegar al destino: "))

# --- Cálculos requeridos ---
combustible_ida = dias * 8
combustible_regreso = dias * 8
reserva_combustible = 10
combustible_total = combustible_ida + combustible_regreso + reserva_combustible

oxigeno = dias * tripulantes * 2 + 5
energia = dias * 5 + 10
provisiones = dias * tripulantes + 3

# --- impresion de resultados ---
print()
print("Misión:", mision)
print("Tripulantes:", tripulantes)
print("Duración estimada hasta el destino:", dias, "días")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Reserva de combustible:", reserva_combustible, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Oxígeno requerido:", oxigeno, "unidades")
print("Energía requerida:", energia, "unidades")
print("Provisiones requeridas:", provisiones, "unidades")

# casos prueba #1
# mision_1 I
#tripulantes=3
#dias=5"
# casos prueba #2
# mision 2
# trip = 1
# dias = 2
# caso prueba (fallido) #3
# trip = 10
# dias = 20



