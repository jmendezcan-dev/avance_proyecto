<img width="565" height="210" alt="image" src="https://github.com/user-attachments/assets/cc36fe8e-1b6f-47c8-98c7-87f8b3657933" />

Avance del proyecto: Preparación de la misión 

Descripción del proyecto

Misión Órbita es un simulador básico de exploración espacial desarrollado en Python que modela, paso a paso, la preparación y ejecución de la misión.

Problema que resuelve: Se necesita una herramienta que ayude a planificar misiones de forma segura, calculando los recursos necesarios, verificando si existen las condiciones para realizarlas y evitando que una nave llegue a su destino sin poder regresar.

Propósito principal: construir progresivamente, a lo largo de tres entregas, un sistema completo que permita preparar la misión, seleccionar un destino, simular el viaje, enfrentar situaciones durante el recorrido y realizar actividades de exploración al llegar.

Alcance de este primer avance: se desarrollan cuatro algoritmos independientes que representan la fase de preparación de la misión, y que luego se convertirán en funciones del sistema final. Se trabajan estructuras secuenciales, cálculos, variables, entradas y salidas,  condicionales simples y dobles, siguiendo el esquema: entrada, procesamiento, decisión y salida.  se analiza y modela antes de programarse: tabla de variables, diagrama de flujo, casos de prueba e implementación y verificación en Python.



Objetivo del proyecto

Desarrollar en Python un simulador de exploración espacial, Misión Órbita, que permita planificar y ejecutar misiones, calculando los recursos necesarios y verificando que existan las condiciones para realizarlas, incluyendo siempre el combustible suficiente para el viaje de regreso. Elaborando las tablas de variables, los diagramas de flujo, los casos de prueba y la implementación verificada de cada algoritmo.



Funcionalidades incluidas

- Funcionalidad ejercicio #1

Cálculo de recursos de la misión: a partir del nombre de la misión, la cantidad de tripulantes y los días estimados para llegar al destino, calcula el combustible necesario (ida, regreso y reserva), además del oxígeno, la energía y las provisiones requeridas.

Verificación de condiciones para realizar la misión: compara los recursos disponibles con los requeridos y, mediante condicionales, decide si la misión puede ejecutarse, asegurando que la nave conserve combustible suficiente para el viaje de regreso.

Evaluación de tripulación varada: si la nave alcanza el destino sin combustible para regresar, lo detecta y estima cuántos días puede sobrevivir la tripulación con el soporte vital disponible.

- Funcionalidad ejercicio #2

Cálculo del combustible total requerido: a partir del combustible necesario para llegar al destino y para regresar, suma la reserva de emergencia de 10 unidades y obtiene el combustible total que exige la misión.

Cálculo del combustible adicional: resta el combustible total requerido al combustible disponible para determinar cuánto combustible sobra (o falta) después de cubrir la misión.

Advertencia de margen bajo: mediante un condicional simple, muestra el mensaje “Advertencia: el margen adicional de combustible es bajo.” únicamente cuando el combustible adicional es menor que 10 unidades.

Presentación de resultados: muestra siempre el combustible disponible, el requerido para llegar, el requerido para regresar, la reserva de emergencia, el combustible total requerido y el combustible adicional disponible.


- Funcionalidad ejercicio #3

  Captura de recursos de soporte vital: solicita el oxígeno y las provisiones disponibles y requeridos para la tripulación.
Verificación de suficiencia de recursos: mediante un condicional doble, comprueba que el oxígeno disponible sea mayor o igual que el requerido y que las provisiones disponibles sean mayores o iguales que las requeridas.

Resultado de autorización de soporte: muestra si la nave posee o no recursos suficientes para la tripulación, sin indicar todavía cuál recurso presenta el problema.

- Funcionalidad ejercicio #4
  Captura de recursos de la misión: solicita el combustible disponible, el combustible requerido para llegar y para regresar, y el oxígeno, la energía y las provisiones disponibles y requeridos.

Cálculo del combustible total requerido: suma el combustible de ida, el de regreso y la reserva de emergencia de 10 unidades, para asegurar que desde el inicio exista combustible suficiente para el viaje de regreso.

Verificación general de autorización: mediante un condicional doble sin anidamiento, comprueba que el combustible, el oxígeno, la energía y las provisiones disponibles sean mayores o iguales que los requeridos.

Resultado del lanzamiento: muestra Lanzamiento autorizado. cuando se cumplen todas las condiciones, o Lanzamiento no autorizado. La misión debe ser revisada. en caso contrario, sin indicar todavía cuál 
recurso provocó el rechazo.

 Tecnologías utilizadas

- Phyton
- Visual Studio Code
  

Requisitos previos de software

Herramientas y software requeridos:


- Visual Studio Code
- Python
- draw.io
- Excel
- Navegador web de preferencia
- Github

Preparación del proyecto

Tener cuenta en git registrada

crear repositorio en Github

usar terminal del sistema 

utilizar comando C:\Users\User\OneDrive\Documentos\avance_proyecto>git clone https://github.com/jmendezcan-dev/avance_proyecto.git  # git clone URL

utilizar comando C:\Users\User\OneDrive\Documentos\avance_proyecto>cd avance_proyecto                                               # cd carpeta

utilizar comando del status del repositorio C:\Users\User\OneDrive\Documentos\avance_proyecto\avance_proyecto>git status            # git status

utilizar comando agregar archivos C:\Users\User\OneDrive\Documentos\avance_proyecto\avance_proyecto>git add                         # git add (archivo a subir)

utilizar comando para commits C:\Users\User\OneDrive\Documentos\avance_proyecto\avance_proyecto>git commit -m "descripción"          # git commit -m "descripción"

ultilizar comando para agregar varios archivos C:\Users\User\OneDrive\Documentos\avance_proyecto\avance_proyecto>git add --all       # git add --all

utilizar comando para push C:\Users\User\OneDrive\Documentos\avance_proyecto\avance_proyecto>git push origin main                    # push al hub 

verificar en Github que los archivos se reflejen correctamente.

Cómo ejecutar el proyecto

Requisitos

- Python ([descargar aquí](https://www.python.org/downloads/))
- Git (opcional, solo para clonar el repositorio)

Para comprobar que Python está instalado:

```bash
python --version
```

 Pasos

1. **Clonar el repositorio** (o descargarlo como ZIP desde el botón **Code**):

```bash
   git clone https://github.com/jmendezcan-dev/avance_proyecto.git
```

2. **Entrar a la carpeta del proyecto:**

```bash
   cd avance_proyecto
```

3. **Entrar a la carpeta de ejercicios:**

```bash
   cd Ejercicios.py
```

4. **Ejecutar el programa que quieras probar:**

```bash
   python nombre_del_archivo.py
```

5. **Ingresar los datos** cuando el programa los solicite en la terminal. Por ejemplo:

```
   Nombre de la misión: Artemis
   Cantidad de tripulantes: 4
   Cantidad de días estimados para llegar al destino: 10
```

   El programa mostrará los resultados directamente en pantalla.

 Otros archivos del repositorio

- `Diagramas_de_flujo/`: diagramas de flujo de cada ejercicio (se abren en [app.diagrams.net](https://app.diagrams.net)).
- `tablas_de_variables.xlsx`: tablas de variables del proyecto (se abre con Excel o LibreOffice).

Estructura del repositorio

```text
avance_proyecto/
├── 01_Diagramas_de_flujo/
├── 02_Tablas_de_variables/
├── 03_Ejercicios/
├── 04_Documentacion/
├── .gitignore
└── README.md
```

- **01_Diagramas_de_flujo/**: diagramas de flujo (`.drawio` y `.png`) de cada ejercicio.
- **02_Tablas_de_variables/**: tabla de variables y casos de prueba.
- **03_Ejercicios/**: código en Python de los cuatro ejercicios.
- **04_Documentacion/**: PDF de avance del proyecto.
- **.gitignore**: archivos ignorados por git.
- **README.md**: descripción general del proyecto.

Estado del proyecto

finalizado.

Información académica

Universidad

CENFOTEC

Principios de programación 1

SOFT-01

Fecha de desarrollo

11/10/26

Estudiantes

- Gabriel Méndez Cantillano
- Isaac Peña Brenes
