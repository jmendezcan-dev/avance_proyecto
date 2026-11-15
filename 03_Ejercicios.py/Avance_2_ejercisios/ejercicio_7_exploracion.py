# ============================================================
# Archivo: ejercicio_7_exploracion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCP0
# Integrantes: Juan Mendez Cantillano e Isaac Peña Brenes
# Fecha: 12/11/2026        Versión: 1.0
# Descripción: Presenta un menú de exploración científica y
#              actualiza recursos, contadores y puntos obtenidos.
# ============================================================

# --- CONSTANTES ---
COSTO_ENERGIA_ANALIZAR = 8
PUNTOS_ANALIZAR = 10

COSTO_ENERGIA_MUESTRA = 12
COSTO_PROVISIONES_MUESTRA = 2
PUNTOS_MUESTRA = 20

COSTO_ENERGIA_OBSERVACION = 5
PUNTOS_OBSERVACION = 8

# --- ENTRADA DE DATOS ---
energia_disponible = int(input("Ingrese la energía disponible: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))

# --- INICIALIZACIÓN ---
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0
exploracion_en_curso = True

# --- MENÚ DE EXPLORACIÓN ---
while exploracion_en_curso == True:
    print("\n----- MENÚ DE EXPLORACIÓN -----")
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")

    opcion = int(input("Seleccione la actividad que va a realizar: "))

    match opcion:
        case 1:
            if (energia_disponible >= COSTO_ENERGIA_ANALIZAR):
                energia_disponible = energia_disponible - COSTO_ENERGIA_ANALIZAR
                actividades_realizadas = actividades_realizadas + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_ANALIZAR
                print(f"Actividad realizada: Analizar terreno. Puntos obtenidos: {PUNTOS_ANALIZAR}")
            else:
                print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
                exploracion_en_curso = False

        case 2:
            if (energia_disponible >= COSTO_ENERGIA_MUESTRA
                    and provisiones_disponibles >= COSTO_PROVISIONES_MUESTRA):
                energia_disponible = energia_disponible - COSTO_ENERGIA_MUESTRA
                provisiones_disponibles = provisiones_disponibles - COSTO_PROVISIONES_MUESTRA
                actividades_realizadas = actividades_realizadas + 1
                muestras_recolectadas = muestras_recolectadas + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_MUESTRA
                print(f"Actividad realizada: Recolectar muestra. Puntos obtenidos: {PUNTOS_MUESTRA}")
            else:
                print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
                exploracion_en_curso = False

        case 3:
            if (energia_disponible >= COSTO_ENERGIA_OBSERVACION):
                energia_disponible = energia_disponible - COSTO_ENERGIA_OBSERVACION
                actividades_realizadas = actividades_realizadas + 1
                puntos_cientificos = puntos_cientificos + PUNTOS_OBSERVACION
                print(f"Actividad realizada: Realizar observación. Puntos obtenidos: {PUNTOS_OBSERVACION}")
            else:
                print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
                exploracion_en_curso = False

        case 4:
            exploracion_en_curso = False

        case _:
            # La opción inválida no consume recursos ni cambia ningun valor.
            print("Opción no válida.")

# --- RESUMEN FINAL ---
print("\n--- RESUMEN DE EXPLORACIÓN ---")
print(f"Actividades realizadas: {actividades_realizadas}")
print(f"Muestras recolectadas: {muestras_recolectadas}")
print(f"Puntos científicos: {puntos_cientificos}")
print(f"Energía restante: {energia_disponible} unidades")
print(f"Provisiones restantes: {provisiones_disponibles} unidades")
