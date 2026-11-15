# Ejercicio 6: Simulación del viaje hacia el destino

# Constantes de consumo diario
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_TRIPULANTE = 1

# Entrada de datos
dias_viaje = int(input("Cantidad de días del viaje: "))
cant_tripulantes = int(input("Cantidad de tripulantes: "))
combustible_disponible = int(input("Combustible disponible: "))
oxigeno_disponible = int(input("Oxígeno disponible: "))
energia_disponible = int(input("Energía disponible: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))

# Consumo diario que depende de la tripulación
consumo_oxigeno_dia = cant_tripulantes * CONSUMO_OXIGENO_TRIPULANTE
consumo_provisiones_dia = cant_tripulantes * CONSUMO_PROVISIONES_TRIPULANTE

# Variables de control del ciclo
dia_actual = 1
dias_completados = 0
puede_continuar = True

# Cada iteración equivale a un día de viaje
while dia_actual <= dias_viaje and puede_continuar:
    # Verificar, antes del consumo, que alcanzan los cuatro recursos
    if (combustible_disponible >= CONSUMO_COMBUSTIBLE_DIA
            and oxigeno_disponible >= consumo_oxigeno_dia
            and energia_disponible >= CONSUMO_ENERGIA_DIA
            and provisiones_disponibles >= consumo_provisiones_dia):
        # Descontar el consumo del día
        combustible_disponible = combustible_disponible - CONSUMO_COMBUSTIBLE_DIA
        oxigeno_disponible = oxigeno_disponible - consumo_oxigeno_dia
        energia_disponible = energia_disponible - CONSUMO_ENERGIA_DIA
        provisiones_disponibles = provisiones_disponibles - consumo_provisiones_dia
        dias_completados = dias_completados + 1

        print("Día", dia_actual, "| Combustible:", combustible_disponible,
              "| Oxígeno:", oxigeno_disponible,
              "| Energía:", energia_disponible,
              "| Provisiones:", provisiones_disponibles)

        dia_actual = dia_actual + 1
    else:
        puede_continuar = False

# Resultado final
if puede_continuar:
    print("La nave llegó al destino en", dias_completados, "días.")
    print("Recursos restantes -> Combustible:", combustible_disponible,
          "| Oxígeno:", oxigeno_disponible,
          "| Energía:", energia_disponible,
          "| Provisiones:", provisiones_disponibles)
else:
    recursos_insuficientes = ""
    if combustible_disponible < CONSUMO_COMBUSTIBLE_DIA:
        recursos_insuficientes = recursos_insuficientes + "Combustible "
    if oxigeno_disponible < consumo_oxigeno_dia:
        recursos_insuficientes = recursos_insuficientes + "Oxígeno "
    if energia_disponible < CONSUMO_ENERGIA_DIA:
        recursos_insuficientes = recursos_insuficientes + "Energía "
    if provisiones_disponibles < consumo_provisiones_dia:
        recursos_insuficientes = recursos_insuficientes + "Provisiones "

    print("Viaje interrumpido en el día " + str(dia_actual) + ".")
    print("Recurso(s) insuficiente(s):", recursos_insuficientes)
    print("Días completados:", dias_completados)