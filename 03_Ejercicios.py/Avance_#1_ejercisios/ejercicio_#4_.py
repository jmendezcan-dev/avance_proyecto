# ===============================================================
# Archivo: ejercisio_#4_.py
# Curso: SOFT-01 Principios de Programacion 1 - Seccion SCP0
# Integrantes: Isaac Peña Brenes, Juan Mendez Cantillano
# Fecha 18/10/2026            Versión: 1.2
# Descripción: Autorización inicial de lanzamiento.
#================================================================

# --- Declaración de constantes ---
RESERVA_COMBUSTIBLE = 10

# --- Entrada de datos ---
combustible_disponible = int(input("Combustible disponible: "))
combustible_ida = int(input("Combustible requerido para llegar al destino: "))
combustible_regreso = int(input("Combustible requerido para regresar: "))
oxigeno_disponible = int(input("Oxígeno disponible: "))
oxigeno_requerido = int(input("Oxígeno requerido: "))
energia_disponible = int(input("Energía disponible: "))
energia_requerida = int(input("Energía requerida: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))
provisiones_requeridas = int(input("Provisiones requeridas: "))

#Cálculo requeridos
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# Decisión (con la condicional doble) 
print()
if (combustible_disponible >= combustible_total
        and oxigeno_disponible >= oxigeno_requerido
        and energia_disponible >= energia_requerida
        and provisiones_disponibles >= provisiones_requeridas):
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")

# caso prueba #1
#100,40,40,40/35,40/35,20/18

# caso prueba #2
#90,40,40,35/35,35/35,18/18

# caso prueba #3
#45,40,40,40/35,40/35,20/18
