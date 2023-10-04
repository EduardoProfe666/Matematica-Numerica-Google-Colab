# Proyecto de MN en Google Colaboratory
[![Languages](https://img.shields.io/github/languages/top/EduardoProfe666/Matematica-Numerica-Google-Colab)](https://github.com/EduardoProfe666/Matematica-Numerica-Google-Colab)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://tlo.mit.edu/learn-about-intellectual-property/software-and-open-source-licensing/open-source-licensing) 
![Static Badge](https://img.shields.io/badge/status-build-green) 
[![Last Commit](https://img.shields.io/github/last-commit/EduardoProfe666/Matematica-Numerica-Google-Colab)](https://github.com/EduardoProfe666/Matematica-Numerica-Google-Colab/commits/master)

> [!WARNING]
> El proyecto aún se encuentra en fase de desarrollo por lo que pueden existir errores y código incompleto

Proyecto que contiene una serie de jupyter notebooks con documentación sobre 
los diferentes algoritmos a utilizar en la asignatura, su implementación en python, 
y una sección para insertar los datos y obtener los resultados de cada algoritmo.

La forma de uso sugerida es a través de [Google Colaboratory](https://colab.research.google.com/?hl=es), 
servicio en línea para la ejecución de código python de manera sencilla, rápida y segura, y sin la necesidad 
de instalar nada, en cualquier plataforma: Windows, Linux, MacOs, Android y IOs

## Directorio de enlaces de los notebooks a Google Colab
> [!NOTE]
> El directorio se encuentra ordenado por capítulos según el libro de texto de MN

- Documentación de bibliotecas usadas:
  - [Arrays de `NumPy`](https://colab.research.google.com/github/EduardoProfe666/Matematica-Numerica-Google-Colab/blob/main/notebooks/tutoriales-generales/Numpy%20Arrays.ipynb)
  - [Funciones de `NumPy`](https://colab.research.google.com/github/EduardoProfe666/Matematica-Numerica-Google-Colab/blob/main/notebooks/tutoriales-generales/Numpy%20Funciones.ipynb)
  - [Graficar en `SimPy`](https://colab.research.google.com/github/EduardoProfe666/Matematica-Numerica-Google-Colab/blob/main/notebooks/tutoriales-generales/Simpy%20Graficar.ipynb)
  - [Graficar en `MatPlotLib`](https://colab.research.google.com/github/EduardoProfe666/Matematica-Numerica-Google-Colab/blob/main/notebooks/tutoriales-generales/Matplotlib%20Graficar.ipynb)
- Cap 1: Teoría de Errores
- Cap 2: Raíces de Ecuaciones
- Cap 3: Sistemas de Ecuaciones Lineales y Matrices
  - [Método de Jacobi](https://colab.research.google.com/github/EduardoProfe666/Matematica-Numerica-Google-Colab/blob/main/notebooks/cap3/Jacobi.ipynb)
  - [Método de Gauss-Seidel](https://colab.research.google.com/github/EduardoProfe666/Matematica-Numerica-Google-Colab/blob/main/notebooks/cap3/Gauss-Seidel.ipynb)
- Cap 4: Aproximación de Funciones
- Cap 5: Integración Numérica
- Cap 6: Optimización Numérica
- Cap 7: Ecuaciones Diferenciales Ordinarias

## Modo de Uso
### Acceder a los notebooks en Google Colab
Para poder acceder a los notebooks en Colab se puede realizar:
- Explorando los archivos en el repositorio:
  > <img src="assets/explorar-archivos.gif" width="100%">
- Utilizando el directorio de enlaces que se encuentra [a continuación en este Readme](#directorio-de-enlaces-de-los-notebooks-a-google-colab)

### Entorno de Desarrollo de Google Colab
Tips:
- Para la navegación organizada dentro del archivo se puede emplear el índice proporcionado por la página
- Para poder empezar a ejecutar el notebook se debe *conectar* a un entorno de ejecución de Google Colab
- Cambiar los datos de entrada en las secciones de inserción de datos para poder obtener los resultados deseados
- Para ejecutar el nuevo código, ir a la pestaña `Entorno de ejecución` y seleccionar la opción `Reiniciar y ejecutar todo`, aceptando todas las ventanas emergentes
- Para poder ver los resultados dirigirse a la sección de salida de datos

#### Versión de Escritorio (Google Chrome)
> <img src="assets/entorno-windows.gif" width="100%">

#### Versión Móvil (Google Chrome)
> <img src="assets/entorno-android.gif">

## Bibliotecas Empleadas:
- `numpy`~=1.26.0
- `matplotlib`~=3.8.0
- `scipy`~=1.11.2
- `simpy`~=4.0.2
- `jupyterlab`~=4.0.6

