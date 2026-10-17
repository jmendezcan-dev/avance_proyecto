# ===============================================================
# Archivo: ejercisio_#1_.py
# Curso: SOFT-01 Principios de Programacion 1 - Seccion SCP0
# Integrantes: Isaac Peña Brenes, Juan Mendez Cantillano
# Fecha 18/10/2026
# Descripción: Calcula los recursos necesarios para una misión.
#================================================================

# --- Constantes declaradas ---
COMBUSTIBLE_POR_DIA = 8
RESERVA_COMBUSTIBLE = 10
OXIGENO_POR_TRIPULANTE_DIA = 2
RESERVA_OXIGENO = 5
ENERGIA_POR_DIA = 5
RESERVA_ENERGIA = 10
RESERVA_PROVISIONES = 3

# --- Entrada de datos ---
mision = input("Nombre de la misión: ")
tripulantes = int(input("Cantidad de tripulantes: "))
dias = int(input("Cantidad de días estimados para llegar al destino: "))

# --- Cálculos requeridos ---
combustible_ida = dias * COMBUSTIBLE_POR_DIA
combustible_regreso = dias * COMBUSTIBLE_POR_DIA
reserva_combustible = RESERVA_COMBUSTIBLE
combustible_total = combustible_ida + combustible_regreso + reserva_combustible

oxigeno = dias * tripulantes * OXIGENO_POR_TRIPULANTE_DIA + RESERVA_OXIGENO
energia = dias * ENERGIA_POR_DIA + RESERVA_ENERGIA
provisiones = dias * tripulantes + RESERVA_PROVISIONES

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



