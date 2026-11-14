# ============================================================
# Archivo: ejercicio_8_regreso.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Juan Mendez Cantillano e Isaac Peña Brenes
# Fecha: 12/11/2026        Versión: 1.0
# Descripción: Evalúa el regreso a la Tierra y, si la nave queda
#              varada, calcula los dias que podrian sobrevivir 
#              y el recurso o los recursos limitantes.
# ============================================================

# --- CONSTANTES ---
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_POR_TRIPULANTE_DIA = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_POR_TRIPULANTE_DIA = 1

# --- ENTRADA DE DATOS ---
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje_ida = int(input("Ingrese la cantidad de días del viaje de ida: "))
combustible = int(input("Ingrese el combustible disponible: "))
oxigeno = int(input("Ingrese el oxígeno disponible: "))
energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))

# --- DECISIÓN DE REGRESO ---
# En el regreso no se exige la reserva de emergencia del lanzamiento.
puede_regresar = combustible >= dias_viaje_ida * CONSUMO_COMBUSTIBLE_DIA

if puede_regresar:
    # --- SIMULACIÓN DEL REGRESO ---
    dia_regreso = 0
    regreso_en_curso = True

    while dia_regreso < dias_viaje_ida and regreso_en_curso:
        if (combustible >= CONSUMO_COMBUSTIBLE_DIA
                and oxigeno >= tripulantes * CONSUMO_OXIGENO_POR_TRIPULANTE_DIA
                and energia >= CONSUMO_ENERGIA_DIA
                and provisiones >= tripulantes * CONSUMO_PROVISIONES_POR_TRIPULANTE_DIA):

            combustible = combustible - CONSUMO_COMBUSTIBLE_DIA
            oxigeno = oxigeno - (tripulantes * CONSUMO_OXIGENO_POR_TRIPULANTE_DIA)
            energia = energia - CONSUMO_ENERGIA_DIA
            provisiones = provisiones - (tripulantes * CONSUMO_PROVISIONES_POR_TRIPULANTE_DIA)

            dia_regreso = dia_regreso + 1

            print(f"Día de regreso {dia_regreso} | Combustible: {combustible} | "
                  f"Oxígeno: {oxigeno} | Energía: {energia} | Provisiones: {provisiones}")
        else:
            print(f"El regreso se interrumpió en el día {dia_regreso + 1}.")

            if combustible < CONSUMO_COMBUSTIBLE_DIA:
                print("Combustible insuficiente.")
            if oxigeno < tripulantes * CONSUMO_OXIGENO_POR_TRIPULANTE_DIA:
                print("Oxígeno insuficiente.")
            if energia < CONSUMO_ENERGIA_DIA:
                print("Energía insuficiente.")
            if provisiones < tripulantes * CONSUMO_PROVISIONES_POR_TRIPULANTE_DIA:
                print("Provisiones insuficientes.")

            regreso_en_curso = False

    # --- RESULTADO DEL REGRESO ---
    if dia_regreso == dias_viaje_ida:
        print("La tripulación regresó exitosamente a la Tierra.")
        print(f"Combustible restante: {combustible} unidades")
        print(f"Oxígeno restante: {oxigeno} unidades")
        print(f"Energía restante: {energia} unidades")
        print(f"Provisiones restantes: {provisiones} unidades")
    else:
        print("La tripulación no completó el regreso.")

else:
    # --- SUPERVIVENCIA EN DESTINO ---
    print("La tripulación quedó varada en el destino.")

    dias_oxigeno = oxigeno // (tripulantes * CONSUMO_OXIGENO_POR_TRIPULANTE_DIA)
    dias_energia = energia // CONSUMO_ENERGIA_DIA
    dias_provisiones = provisiones // tripulantes

    # Se obtiene el menor valor mediante condicionales
    supervivencia_estimada = dias_oxigeno

    if dias_energia < supervivencia_estimada:
        supervivencia_estimada = dias_energia

    if dias_provisiones < supervivencia_estimada:
        supervivencia_estimada = dias_provisiones

    # Se agregan todos los recursos cuyo resultado coincide con el mínimo.
    recursos_limitantes = ""

    if dias_oxigeno == supervivencia_estimada:
        recursos_limitantes = "oxígeno"

    if dias_energia == supervivencia_estimada:
        if recursos_limitantes == "":
            recursos_limitantes = "energía"
        else:
            recursos_limitantes = recursos_limitantes + ", energía"

    if dias_provisiones == supervivencia_estimada:
        if recursos_limitantes == "":
            recursos_limitantes = "provisiones"
        else:
            recursos_limitantes = recursos_limitantes + ", provisiones"

    # --- RESULTADO DE SUPERVIVENCIA ---
    print(f"Días por oxígeno: {dias_oxigeno}")
    print(f"Días por energía: {dias_energia}")
    print(f"Días por provisiones: {dias_provisiones}")
    print(f"Supervivencia estimada: {supervivencia_estimada} días")
    print(f"Recurso(s) limitante(s): {recursos_limitantes}")
