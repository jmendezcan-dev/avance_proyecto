# ===============================================================
# Archivo: ejercisio_#2_.py
# Curso: SOFT-01 Principios de Programacion 1 - Seccion SCP0
# Integrantes: Isaac Peña Brenes, Juan Mendez Cantillano
# Fecha 18/10/2026            Versión: 1.2
# Descripción: Verificación de combustible.
#================================================================

# --- Constantes declaradas ---
RESERVA_COMBUSTIBLE = 10

# --- Entrada de datos ---
disponible = int(input("Combustible disponible: "))
combustible_ida = int(input("Combustible requerido para llegar al destino: "))
combustible_regreso = int(input("Combustible requerido para regresar: "))

#  Calculos requeridos
total_requerido = combustible_ida + RESERVA_COMBUSTIBLE
adicional = disponible - total_requerido


# Salidas 

print("Combustible disponible:", disponible, "unidades")
print("Combustible requerido para llegar:", combustible_ida, "unidades")
print("Combustible requerido para regresar:", combustible_regreso, "unidades")
print("Reserva de emergencia:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", total_requerido, "unidades")
print("Combustible adicional disponible:", adicional, "unidades")

# --- Regla de advertencia (solo si el margen es bajo) ---
if adicional < RESERVA_COMBUSTIBLE:
    print("Advertencia: el margen adicional de combustible es bajo.")

# prueba 

# margen_bajo 
# Disponible: 95,  40, regreso: 40

# margen limite
# Disponible: 100,  40, regreso: 40

#margen insuficiente
#Disponible: 80,  40, regreso: 40