# Proyecto Identificador de Nubes
----
# Universidad Nacional Autónoma de México

## Facultad de Ciencias

### Ciencias de la Computación

----
Autores: Diego Arturo Velázquez Trejo (https://github.com/DiegoArturoVelazquezTrejo)
Mario Escobar Rosales (https://github.com/luismarioescobarrosales2000)
========================

#### Descripción:
  - Se desarrolló un sistema que con base en operaciones sobre imágenes utilizando OpenCV, lleva a cabo una clasificación de pixeles (pixeles de nube y pixeles de cielo).

  Nuestro objetivo es calcular el índice de cobertura nubosa de una serie de fotografías con las siguientes características:

  a) Fotografía con dimensiones: 4,368 px x 2912 px
  b) El cielo centrado en la imagen y con un radio de 1324 px.

### Requisitos para la ejecución correcta del programa:
  1) Versión Python3.0.0 en adelante.
  2) Biblioteca OpenCV (https://opencv.org/releases/)
  3) Biblioteca Numpy
  4) Biblioteca Math

### Para ejecutar:
```
$ python3 src/Main.py [Ruta de la imagen] [Bandera opcional]
```
La bandera opcional es -S y sirve para que el programa despliegue la imagen segmentada binariamente.
