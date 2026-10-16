# avance_proyecto

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

#######################Plantilla###############################

Avance del proyecto: Preparación de la misión 

Descripción del proyecto

Descripción del proyecto

Misión Órbita es un simulador básico de exploración espacial desarrollado en Python que modela, paso a paso, la preparación y ejecución de la misión.

Problema que resuelve: Necesita una herramienta que ayude a planificar misiones de forma segura, calculando los recursos necesarios, verificando si existen las condiciones para realizarlas y evitando que una nave llegue a su destino sin poder regresar.

Propósito principal: construir progresivamente, a lo largo de tres entregas, un sistema completo que permita preparar la misión, seleccionar un destino, simular el viaje, enfrentar situaciones durante el recorrido y realizar actividades de exploración al llegar.

Alcance de este primer avance: se desarrollan cuatro algoritmos independientes que representan la fase de preparación de la misión, y que luego se convertirán en funciones del sistema final. Se trabajan estructuras secuenciales, cálculos, variables, entradas y salidas,  condicionales simples y dobles, siguiendo el esquema: entrada, procesamiento, decisión y salida.  se analiza y modela antes de programarse: tabla de variables, diagrama de flujo, casos de prueba e implementación y verificación en Python.



Objetivo del proyecto

Desarrollar en Python un simulador de exploración espacial, Misión Órbita, que permita planificar y ejecutar misiones, calculando los recursos necesarios y verificando que existan las condiciones para realizarlas, incluyendo siempre el combustible suficiente para el viaje de regreso. Elaborando las tablas de variables, los diagramas de flujo, los casos de prueba y la implementación verificada de cada algoritmo.



Funcionalidades incluidas

- Funcionalidad ejercisio #1

Cálculo de recursos de la misión: a partir del nombre de la misión, la cantidad de tripulantes y los días estimados para llegar al destino, calcula el combustible necesario (ida, regreso y reserva), además del oxígeno, la energía y las provisiones requeridas.

Verificación de condiciones para realizar la misión: compara los recursos disponibles con los requeridos y, mediante condicionales, decide si la misión puede ejecutarse, asegurando que la nave conserve combustible suficiente para el viaje de regreso.

Evaluación de tripulación varada: si la nave alcanza el destino sin combustible para regresar, lo detecta y estima cuántos días puede sobrevivir la tripulación con el soporte vital disponible.

- Funcionalidad ejercisio #2

Cálculo del combustible total requerido: a partir del combustible necesario para llegar al destino y para regresar, suma la reserva de emergencia de 10 unidades y obtiene el combustible total que exige la misión.

Cálculo del combustible adicional: resta el combustible total requerido al combustible disponible para determinar cuánto combustible sobra (o falta) después de cubrir la misión.

Advertencia de margen bajo: mediante un condicional simple, muestra el mensaje “Advertencia: el margen adicional de combustible es bajo.” únicamente cuando el combustible adicional es menor que 10 unidades.

Presentación de resultados: muestra siempre el combustible disponible, el requerido para llegar, el requerido para regresar, la reserva de emergencia, el combustible total requerido y el combustible adicional disponible.


- Funcionalidad ejercisio #3

  Captura de recursos de soporte vital: solicita el oxígeno y las provisiones disponibles y requeridos para la tripulación.
Verificación de suficiencia de recursos: mediante un condicional doble, comprueba que el oxígeno disponible sea mayor o igual que el requerido y que las provisiones disponibles sean mayores o iguales que las requeridas.

Resultado de autorización de soporte: muestra si la nave posee o no recursos suficientes para la tripulación, sin indicar todavía cuál recurso presenta el problema.

- Funcionalidad ejercisio #4
  Captura de recursos de la misión: solicita el combustible disponible, el combustible requerido para llegar y para regresar, y el oxígeno, la energía y las provisiones disponibles y requeridos.

Cálculo del combustible total requerido: suma el combustible de ida, el de regreso y la reserva de emergencia de 10 unidades, para asegurar que desde el inicio exista combustible suficiente para el viaje de regreso.

Verificación general de autorización: mediante un condicional doble sin anidamiento, comprueba que el combustible, el oxígeno, la energía y las provisiones disponibles sean mayores o iguales que los requeridos.

Resultado del lanzamiento: muestra Lanzamiento autorizado. cuando se cumplen todas las condiciones, o Lanzamiento no autorizado. La misión debe ser revisada. en caso contrario, sin indicar todavía cuál 
recurso provocó el rechazo.

 Tecnologías utilizadas

- phyton
- visual code
  

Requisitos previos de software

Indique el software o herramientas que deben estar instaladas para poder utilizar o ejecutar el proyecto.

software necesarios :

- Visual Studio Code
- Python
- draw.io
- excell
- Navegador web preferencia
- github

Preparación del proyecto

Tener cuenta en git registrada

crear rpositorio en Github

usar terminal del sistema 

utilizar comando C:\Users\User\OneDrive\Documentos\avance_proyecto>git clone https://github.com/jmendezcan-dev/avance_proyecto.git  # git clone URL

utilziar comando C:\Users\User\OneDrive\Documentos\avance_proyecto>cd avance_proyecto                                               # cd carpeta

utilizar comando del status del repositorio C:\Users\User\OneDrive\Documentos\avance_proyecto\avance_proyecto>git status            # git status

utilizar comando agregar archivos C:\Users\User\OneDrive\Documentos\avance_proyecto\avance_proyecto>git add                         # git add (archivo a subir)

utilizar comando para commits C:\Users\User\OneDrive\Documentos\avance_proyecto\avance_proyecto>git commit -m "descrpcion"          # git commit -m "descripcion"

ultilizar comando para agregar varios archivos C:\Users\User\OneDrive\Documentos\avance_proyecto\avance_proyecto>git add --all       # git add --all

utilizar comando para push C:\Users\User\OneDrive\Documentos\avance_proyecto\avance_proyecto>git push origin main                    # push al hub 

verificar en github que los archivos se reflejen correctamente.

## Cómo ejecutar el proyecto

Explique de forma clara los pasos necesarios para ejecutar el proyecto.

Ejemplo:

```bash
python main.py
```

o:

```bash
npm install
npm run dev
```

## Estructura del repositorio

Explique brevemente la organización principal de carpetas y archivos del repositorio.

Ejemplo:

```text
proyecto/
├── src/
├── docs/
├── README.md
└── archivo_principal
```

## Estado del proyecto

Indique el estado actual del proyecto.

Ejemplos:

- En desarrollo
- Avance 1
- Avance 2
- Entrega final
- Finalizado

Información académica

Universidad

Cenfotec

Principios de programación 1

soft-01

Fecha de desarrollo

10/10/26

Estudiantes

- Gabriel Méndez cantillano
- Isaac pena brenes
