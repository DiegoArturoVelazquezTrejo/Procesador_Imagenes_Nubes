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

### Observaciones y proceso de análisis:
 Primeramente, utilizamos photoshop para modificar la imagen de tal manera que pudiéramos identificar
 los contornos así como aquellas regiones en donde las nubes presentes.

 Observación 1: Para visualizar de una forma más real la imagen , tuvimos que realizar un procedimiento de contraste para que en aquellas zonas donde la luz es presente, identificar si son nubes o es cielo, ya que realmente podía ser cualquiera de los dos.

 Si el usuario desea, puede utilizar el método de disminuir contraste (Clase ProcesaImagen) sobre la ProcesaImagen real para así visualizarla sin ruido.

 Realizamos la implementación de varios métodos para el procesado de los colores de una imagen: Si el usuario
 desea utilizarlas, las escalas de colores que manejamos son:

 a) YIQ
 b) YUV
 c) RGB

 Observación 2: Hay varias líneas comentadas en el Main.py en donde, si el usuario las descomenta, puede ver
 otro tipo de operaciones sobre la imagen.

 Pruebas unitarias:
 Para ejecutar las pruebas unitarias, basta con posicionarse en la carpeta dle Proyecto, afuera de src y escribir:
### Para ejecutar pruebas unitarias:
 ```
 $ python3 src/Test.py 
 ```
