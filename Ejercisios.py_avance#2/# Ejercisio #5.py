# Ejercisio #5
# SELECCIÓN DEL DESTINO Y AUTORIZACIÓN DE LA MISIÓN

# Constantes
CONSUMO_COMBUSTIBLE_DIA = 8
RESERVA_COMBUSTIBLE = 10
CONSUMO_OXIGENO_TRIPULANTE = 2
RESERVA_OXIGENO = 5
CONSUMO_ENERGIA_DIA = 5
ENERGIA_EXPLORACION = 10
CONSUMO_PROVISIONES_TRIPULANTE = 1
RESERVA_PROVISIONES = 3

print("SELECCIÓN DEL DESTINO Y AUTORIZACIÓN DE LA MISIÓN")

nombre_mision = input("Nombre de la misión: ")
cant_tripulantes = int(input("Cantidad de tripulantes: "))

print("DESTINOS DISPONIBLES")
print("1. Luna (3 días de viaje)")
print("2. Marte (5 días de viaje)")
print("3. Europa (7 días de viaje)")
opcion_destino = int(input("Opción de destino: "))

# Condicional múltiple
opcion_valida = True
nombre_destino = ""
dias_viaje = 0

match opcion_destino:
    case 1:
        nombre_destino = "Luna"
        dias_viaje = 3
    case 2:
        nombre_destino = "Marte"
        dias_viaje = 5
    case 3:
        nombre_destino = "Europa"
        dias_viaje = 7
    case _:
        opcion_valida = False

# Condicional anidada: rama de opción válida
if not opcion_valida:
    print("Opción de destino no válida. La misión no puede planificarse.")
else:
    print("Ingrese los recursos disponibles para la misión:")
    combustible_disponible = int(input("Combustible disponible: "))
    oxigeno_disponible = int(input("Oxígeno disponible: "))
    energia_disponible = int(input("Energía disponible: "))
    provisiones_disponibles = int(input("Provisiones disponibles: "))

    combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
    combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
    combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

    oxigeno_requerido = (dias_viaje * cant_tripulantes * CONSUMO_OXIGENO_TRIPULANTE) + RESERVA_OXIGENO
    energia_requerida = (dias_viaje * CONSUMO_ENERGIA_DIA) + ENERGIA_EXPLORACION
    provisiones_requeridas = (dias_viaje * cant_tripulantes * CONSUMO_PROVISIONES_TRIPULANTE) + RESERVA_PROVISIONES

    lanzamiento_autorizado = (
        combustible_disponible >= combustible_total_requerido
        and oxigeno_disponible >= oxigeno_requerido
        and energia_disponible >= energia_requerida
        and provisiones_disponibles >= provisiones_requeridas
    )

    print("Misión:", nombre_mision)
    print("Destino:", nombre_destino)
    print("Tripulantes:", cant_tripulantes)
    print("Duración del viaje de ida:", dias_viaje, "días")

    print("REQUISITOS DE RECURSOS")
    print("Combustible para llegar:", combustible_ida)
    print("Combustible para regresar:", combustible_regreso)
    print("Reserva de combustible:", RESERVA_COMBUSTIBLE)
    print("Combustible total requerido:", combustible_total_requerido)
    print("Oxígeno requerido:", oxigeno_requerido)
    print("Energía requerida:", energia_requerida)
    print("Provisiones requeridas:", provisiones_requeridas)

    if lanzamiento_autorizado:
        print("Lanzamiento autorizado.")
    else:
        print("Lanzamiento no autorizado. La misión debe ser revisada.")