# ===============================================================
# Archivo: ejercisio_#3_.py
# Curso: SOFT-01 Principios de Programacion 1 - Seccion SCP0
# Integrantes: Isaac Peña Brenes, Juan Mendez Cantillano
# Fecha 18/10/2026
# Descripción: Verificación del soporte para la tripulación.
#================================================================

# --- Entrada de datos ---
oxigeno_disponible = int(input("Cantidad de oxígeno disponible: "))
oxigeno_requerido = int(input("Cantidad de oxígeno requerido: "))
provisiones_disponibles = int(input("Cantidad de provisiones disponibles: "))
provisiones_requeridas = int(input("Cantidad de provisiones requeridas: "))

# --- Decisión (condicional doble) ---
print()
if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")

# casos prueba #1
# 45 ,38 ,20, 18


# casos prueba #2
# 35.35,18,18


# caso prueba (fallido) #3
# 30,35,20,18
