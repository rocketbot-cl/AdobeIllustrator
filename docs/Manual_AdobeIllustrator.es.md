# Adobe Illustrator
  
Módulo para automatizar tareas en Adobe Illustrator  

*Read this in other languages: [English](Manual_AdobeIllustrator.md), [Português](Manual_AdobeIllustrator.pr.md), [Español](Manual_AdobeIllustrator.es.md)*
  

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

### Abrir Archivo AutoCAD
  
Este comando permite abrir un archivo en formato AutoCAD en Adobe Illustrator
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo|Ruta del archivo que se desea abrir en Adobe Illustrator|C:/Users/Usuario/Desktop/imagen.dxf|
|Opción de escala global|Selecciona una opción de escala global|Tamaño original|
|Unidades|Unidades del archivo|1|
|Unidad de medida|Selecciona la unidad de medida del archivo|Centimeters|
|Escala global (porcentaje)|Escala global en porcentaje|100|
|Asignar resultado a variable|Nombre de la variable donde se guardará True o False dependiendo si el archivo se abrió correctamente|variable|

### Cambiar modo de color de documento
  
Este comando permite cambiar el modo de color del documento actual de Adobe Illustrator
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Modo de color|Modo de color que desea aplicar al documento actual de Adobe Illustrator|RGB|

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
