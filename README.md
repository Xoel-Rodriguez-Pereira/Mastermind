# Mastermind
## Introducción:
Aplicación desarroyada por: \
[Xoel Rodríguez](https://github.com/Xoel-Rodriguez-Pereira) \
[Lucas Iñarrea](https://github.com/EdMorCa67)

Durante el curso 25-26 de DAM en el IES de Teis.

## Manual de instalación y uso:
REQUISITOS PREVIOS

Antes de comenzar, asegúrate de tener instalado:

- Git \
  `git --version`

- Python 3.11 o superior \
  `python --version`

Nota:
Aunque uv gestiona automáticamente el entorno virtual, Python debe estar instalado previamente en el sistema.

---------------------------------------------------------------------

1) INSTALAR UV

macOS y Linux:

`curl -LsSf https://astral.sh/uv/install.sh | sh`

Recarga la terminal:

`source ~/.bashrc` \
o \
`source ~/.zshrc`

Windows (PowerShell):

`powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

Verificar la instalación:

`uv --version`

---------------------------------------------------------------------

2) DESCARGAR EL PROYECTO MASTERMIND DESDE GITHUB

Clona el repositorio:

`git clone https://github.com/Xoel-Rodriguez-Pereira/Mastermind.git`

Accede a la carpeta del proyecto:

`cd Mastermind`

---------------------------------------------------------------------

3) INSTALAR LAS DEPENDENCIAS DEL PROYECTO

Desde la raíz del proyecto ejecuta:

`uv sync`

Este comando:
- Crea automáticamente un entorno virtual
- Instala todas las dependencias necesarias
- Usa uv.lock para una instalación reproducible

---------------------------------------------------------------------

4) EJECUTAR EL PROYECTO MASTERMIND

`uv run python main.py`

---------------------------------------------------------------------

5) PROBLEMAS COMUNES

Error: "uv: command not found"
- Reinicia la terminal
- Verifica que uv esté correctamente añadido al PATH

Error de versión de Python:
Revisa el archivo pyproject.toml, por ejemplo:

requires-python = ">=3.11"

Instala una versión compatible de Python.

## Normas del juego:

El juego consiste en crear un código que la aplicación tratará de adivinar.

El código debe estar formado por una combinacion de 4 colores, permitiendo repertir color, de los 8 colores disponibles.

Los colores disponibles son:
- ROJO
- VERDE
- AZUL
- AMARILLO
- ROSA
- CELESTE
- BLANCO
- NEGRO

Para introducir el código escribe una los cuatro colores separados por espacio. \
Ejemplo: `Rojo Amarillo Verde Blanco` 

*Puede escribirse en mayúscula o en minúscula.*



## Diseño:
### Diagrama de componentes:

  ![Diagrama de componentes](assets/Diagrama%20de%20componentes.png)


## Uso de IA:
Ninguna parte del código está directamente creada por IA, pero si hemos usado ChatGPT y Copilot como apoyos para aclarar dudas sobre el funcionamiento de funciones *Buit In* de python, funcionalidades de Vscode, etc.

También se ha utilizado ChatGPT para asistir con la redacción del README.


## Conclusión:

Durante el transcurso de este proyecto durante las clases de programación y metodología
hemos llegado a entender el concepto del algoritmo genético y como funciona la inteligencia
artificial a través del mastermind, los módulos que conllevan para hacerla funcionar junto con las ventajas como las dificultades que 
lleva llegar a comprenderla.

## Posibles mejoras

- Los casos tests son muy favorables
- Como se printea en pantalla
- Evitar que se repita la misma selección