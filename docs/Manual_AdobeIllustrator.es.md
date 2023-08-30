# Adobe Illustrator
  
Módulo para automatizar tareas en Adobe Illustrator  

*Read this in other languages: [English](Manual_AdobeIllustrator.md), [Português](Manual_AdobeIllustrator.pr.md), [Español](Manual_AdobeIllustrator.es.md)*
  
![banner](imgs/Banner_AdobeIllustrator.jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Abrir Illustrator
  
Este comando permite abrir el programa Adobe Illustrator
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del programa|Ruta del programa Adobe Illustrator.exe|C:/Program Files/Adobe/Adobe Illustrator CC 2019/Support Files/Contents/Windows/Illustrator.exe|
|Asignar resultado a variable|Nombre de la variable donde se guardará True o False dependiendo si el programa se abrió correctamente|variable|

### Abrir Archivo .ai
  
Este comando permite abrir un archivo en formato .ai en Adobe Illustrator
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo|Ruta del archivo que se desea abrir en Adobe Illustrator|C:/Users/Usuario/Desktop/imagen.ai|
|Modo de color de documento|Seleccione el modo de color con el cual se abrirá el documento en Adobe Illustrator|RGB|
|Asignar resultado a variable|Nombre de la variable donde se guardará True o False dependiendo si el archivo se abrió correctamente|variable|

### Abrir Archivo AutoCAD
  
Este comando permite abrir un archivo en formato AutoCAD en Adobe Illustrator
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo|Ruta del archivo que se desea abrir en Adobe Illustrator|C:/Users/Usuario/Desktop/imagen.dxf|
|Opción de escala global|Selecciona una opción de escala global|Tamaño original|
|Unidades|Unidades del archivo|1|
|Unidad de medida|Selecciona la unidad de medida del archivo|Centimeters|
|Escala global (porcentaje)|Escala global en porcentaje|100|
|Centrar diseño|Centra el diseño en el área de trabajo|True|
|Escalar grosores de línea|Escala los grosores de las líneas en función de la escala global|False|
|Combinar capas|Combina todas las capas en una sola|False|
|Asignar resultado a variable|Nombre de la variable donde se guardará True o False dependiendo si el archivo se abrió correctamente|variable|

### Cambiar modo de color de documento
  
Este comando permite cambiar el modo de color del documento actual de Adobe Illustrator
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Modo de color|Modo de color que desea aplicar al documento actual de Adobe Illustrator|RGB|

### Cambiar color CMYK de capa
  
Este comando permite cambiar el color CMYK la capa seleccionada en el documento actual de Adobe Illustrator
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Color Cyan|Valor de 0 a 100 para el color Cyan|100|
|Color Magenta|Valor de 0 a 100 para el color Magenta|100|
|Color Yellow|Valor de 0 a 100 para el color Yellow|100|
|Color Black|Valor de 0 a 100 para el color Black|100|

### Agregar mesa de trabajo
  
Este comando permite agregar una mesa de trabajo al documento actual de Adobe Illustrator
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la mesa de trabajo|Nombre de la mesa de trabajo que desea agregar al documento actual de Adobe Illustrator|Mesa de trabajo 2|
|Largo de la mesa de trabajo|Largo de la mesa de trabajo que desea agregar al documento actual de Adobe Illustrator|100|
|Ancho de la mesa de trabajo|Ancho de la mesa de trabajo que desea agregar al documento actual de Adobe Illustrator|100|
|Posicion X de la mesa de trabajo|Posicion X de la mesa de trabajo que desea agregar al documento actual de Adobe Illustrator|0|
|Posicion Y de la mesa de trabajo|Posicion Y de la mesa de trabajo que desea agregar al documento actual de Adobe Illustrator|0|

### Seleccionar mesa de trabajo
  
Este comando permite seleccionar una mesa de trabajo del documento actual de Adobe Illustrator
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la mesa de trabajo|Nombre de la mesa de trabajo que desea seleccionar del documento actual de Adobe Illustrator|Mesa de trabajo 1|

### Duplicar mesa de trabajo
  
Este comando permite duplicar una mesa de trabajo del documento actual de Adobe Illustrator
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la mesa de trabajo|Nombre de la mesa de trabajo que desea duplicar del documento actual de Adobe Illustrator|Mesa de trabajo 1|
|Nombre de la nueva mesa de trabajo|Nombre que tendrá la nueva mesa de trabajo que se creará a partir de la mesa de trabajo que se desea duplicar|Mesa de trabajo 2|
|Posición de la mesa de trabajo|Seleccione donde colocar la nueva mesa de trabajo|Abajo|
|Copiar contenido|Seleccione si desea copiar el contenido de la mesa de trabajo|True|

### Encajar en limites de ilustración
  
Este comando permite encajar el contenido de la mesa de trabajo en los limites de la ilustración seleccionada. Debe seleccionarse previamente la capa de arte.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la mesa de trabajo|Nombre de la mesa de trabajo a la que se desea ajustar el contenido del documento actual de Adobe Illustrator.|Mesa de trabajo 1|

### Eliminar capa
  
Este comando permite eliminar una capa del documento actual de Adobe Illustrator
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la capa|Nombre de la capa que desea eliminar del documento actual de Adobe Illustrator|Capa 1|

### Seleccionar capa
  
Este comando permite seleccionar una capa del documento actual de Adobe Illustrator
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Capa a seleccionar|Nombre de la capa que desea seleccionar del documento actual de Adobe Illustrator|Capa 1|

### Asignar visibilidad de capa
  
Este comando permite asignar la visibilidad de una capa del documento actual de Adobe Illustrator
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de capa|Nombre de la capa que desea setear la visibilidad del documento actual de Adobe Illustrator|Capa 1|
|Visibilidad|Visibilidad que desea asignar a la capa del documento actual de Adobe Illustrator|Visible|

### Seleccionar capa de arte
  
Este comando permite seleccionar la capa de arte del documento actual de Adobe Illustrator
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la capa|Nombre de la capa que se desea seleccionar del documento actual de Adobe Illustrator|Capa 1|

### Ejecutar Script JS
  
Este comando permite ejecutar un script JavaScript en el documento actual de Adobe Illustrator
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Archivo JS|Seleccione el archivo JS que desea ejecutar en el documento actual de Adobe Illustrator|C:/Users/User/Desktop/script.js|

### Herramienta Reflejar
  
Este comando permite reflejar el objeto seleccionado en el documento actual de Adobe Illustrator
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Eje|Seleccione el eje de reflexión (horizontal o vertical)|Horizontal|

### Guardar como EPS
  
Este comando permite guardar un archivo del Adobe Illustrator en formato EPS
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta y nombre del archivo a guardar|Ruta y nombre del archivo a guardar. La ruta debe existir|C:/Users/usuario/Desktop/file.eps|
|Guardar múltiples mesas de trabajo|Si está activo, se guardarán todas las mesas de trabajo a excepción de si se especifica un rango.|True|
|Rango de mesas de trabajo|Rango de mesas de trabajo a guardar. Ejemplo 1-3,5,7-9|1-4|
|Incluir CMYK PostScript en archivos RGB|Si está activo, se incluirá un perfil CMYK PostScript en archivos RGB|True|
|Incrustar todas las fuentes|Si está activo, todas las fuentes utilizadas por el documento se incrustarán en el archivo guardado|True|
|Incrustar archivos vinculados|Si está activo, las imágenes vinculadas se incluirán en el documento guardado.|True|
|Compatibilidad|Versión de compatibilidad del archivo EPS|Illustrator CS6 (16)|
|Formato de vista previa|El formato para la imagen de vista previa EPS.|TIFF (8-bit Color)|
|Incluir miniaturas de documentos|Si está activo, se incluirá una imagen en miniatura del documento EPS.|True|
|Impresión de degradado compatible|Si está activo, se creará un elemento de trama del degradado o malla de degradado para que las impresoras PostScript de nivel 2 puedan imprimir el objeto.|True|
|Nivel de Adobe PostScript|Nivel de lenguaje PostScript para usar (Nivel 1 válido para la versión del formato de archivo 8 o anterior).|Level 2|
|Asignar resultado a variable|Nombre de la variable donde se guardará True o False dependiendo si el archivo se guardó correctamente|variable|

### Guardar .ai
  
Este comando permite guardar un archivo de Adobe Illustrator en formato .ai
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta y nombre del archivo a guardar|Ruta y nombre del archivo a guardar. La ruta debe existir|C:/Users/usuario/Desktop/imagen.ai|
|Asignar resultado a variable|Nombre de la variable donde se guardará True o False dependiendo si el archivo se guardó correctamente|variable|

### Cerrar Illustrator
  
Este comando permite cerrar el programa Adobe Illustrator
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a variable|Nombre de la variable donde se guardará True o False dependiendo si el programa se cerró correctamente|variable|
