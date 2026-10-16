# avance_proyecto

Primer avance del proyecto: Preparacion de la mision

Integrantes:

Isaac Pena Brenes

Gabriel mendez cantillano

curso: soft-01

Ejercisio #1

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


Instrucciones: 
Ejercisio 1: calculo de recursos necesarios (ejercisio_#1_.py)

Este programa calcula los recursos automaticos de combustible, oxigeno, energia y provisiones a partir de los datos basicos de la mision utilizando un flujo puramente secuencial.

Comando para ejecutar:

Distintos casos 

Caso de Prueba #1 (Validacion Exitosa):
1. Ingrese "Explorador 1" en el nombre de la mision.
2. Ingrese "3" en la cantidad de tripulantes.
3. Ingrese "5" en la cantidad de dias.
El sistema debera calcular un total de 90 unidades de combustible, 35 de oxigeno, 35 de energia y 18 de provisiones.

Caso de Prueba #2 (Escenario Base Minimo):
1. Ingrese "Segunda mision" en el nombre de la mision.
2. Ingrese "1" en la cantidad de tripulantes.
3. Ingrese "2" en la cantidad de dias.
El sistema debera calcular un total de 42 unidades de combustible, 9 de oxigeno, 20 de energia y 5 de provisiones.

Caso de Prueba #3 (Escenario de Alta Demanda):
1. Ingrese "Mision critica" en el nombre de la mision.
2. Ingrese "10" en la cantidad de tripulantes.
3. Ingrese "20" en la cantidad de dias.
El sistema calculara de manera proporcional el alto consumo para misiones prolongadas.
