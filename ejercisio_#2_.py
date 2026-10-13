# Ejercicio 2

# --- Entrada de datos ---
disponible = int(input("Combustible disponible: "))
combustible_ida = int(input("Combustible requerido para llegar al destino: "))
combustible_regreso = int(input("Combustible requerido para regresar: "))

#  Calculos requeridos
reserva = 10
total_requerido = combustible_ida + combustible_regreso + reserva
adicional = disponible - total_requerido

# Salidas 

print("Combustible disponible:", disponible, "unidades")
print("Combustible requerido para llegar:", combustible_ida, "unidades")
print("Combustible requerido para regresar:", combustible_regreso, "unidades")
print("Reserva de emergencia:", reserva, "unidades")
print("Combustible total requerido:", total_requerido, "unidades")
print("Combustible adicional disponible:", adicional, "unidades")

# --- Regla de advertencia (solo si el margen es bajo) ---
if adicional < 10:
    print("Advertencia: el margen adicional de combustible es bajo.")

# prueba 

# margen_bajo 
# Disponible: 95,  40, regreso: 40

# margen limite
# Disponible: 100,  40, regreso: 40

#margen insuficiente
#Disponible: 80,  40, regreso: 40