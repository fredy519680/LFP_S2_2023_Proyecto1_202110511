# Laboratorio Lenguajes Formales y de Programación
## Proyecto 1
### 2do Semestre 2023
```js
Universidad San Carlos de Guatemala
Programador: Fredy Alexander Esteban Pineda
Carne: 202110511
Correo: 3927736270101@ingenieria.usac.edu.gt
```
---
## Descripción del Proyecto
En este proyecto se nos propone como problemática el crear aun analizador Léxico 
el cual sea capaz de leer y realizar distintas operaciones matemáticas por medio de la lectura de un archivo de entrada tipo Json. Para esto deberemos realizar un Scanner que sea capaz de leer caracter por caracter y devolvernos los errores léxicos que encuentre. De igual forma las operaciones que realice nuestro programa deberán de mostrarse de forma gráfica por medio de la herramienta de graphviz en forma de un arbol binario. 

## Objetivos
* Objetivo General
    * Realizar un analizador léxico capaz de reconocer tokens y realizar las diferentes funciones validas que se proponen en el enunciado
* Objetivos Específicos
    * Poner en práctica los conocimientos sobre analizadores léxicos y automatas finitos para la realización del Escaner 
    * Generar un resultado visual de las operaciones validas que obtenga nuestro analiador léxico por medio de la herramienta graphviz
    * Generar un arhivo de errores el cual contenga errores léxicos en el archivo de entrada este archivo deberá ser manejado en formato json


---
## Manual de usuario
Este manual se usuario sirve como guia para un usuario que desea utilizar nuestro software para resolver problemas aritmeticos y representarlos en diagramas de arboles, iremos detallando las funcionalidades del programa acompañado con contenido visual para poder entenderlo de una mejor manera. 

Pantala de Inicio:
Esta pantalla es la pantalla principal en la cual es usuario ingresara por primera vez, en la parte de arriba podemos observar 4 botones con diferentes funcionalidades y en la parte de abajo una caja de texto en la cual podremos abrir nuestros archivos y modificarlos 

![MU-inicio-menu](https://i.ibb.co/drBGzZx/MU-Inicio-menu.png)

Boton de archivo: 
En este botón si le damos click nos deplegará un menú en el cual podremos ver 4 opciones para manejar archivo 

-Abrir: Esta opcion nos abre el explorador de archivos y nos permite escoger cualquier archivo de tipo json

-Guardar: Esta opción guarda el archivo con el mismo nombre con el que se abrió 

-Guardar como: Guardar como nos permite guardar el archivo en formato json con el nombre que nosotros querramos 

-Salir: Esta opción nos permite finalizar el programa y cierra la ventana 

![Iniciomenu](https://i.ibb.co/NjP4ZyN/MU-Boton-archivo.png)



Si presionamos el boton de abrir este nos dejara seleccionar cualquier archivo en nuestra computadora que sea formato json y luego de seleccionarlo este lo desplegará en el cuadro de texto donde tambien lo podremos modificar. 

![}Abrir](https://i.ibb.co/JjgQT63/MU-Abrir-el-archivo.png)

Boton Analizar:

Este botón al presionarlo leera el texto con el archivo json que se encuentra en la caja de texto, luego mostrara los caracteres que reconocidos por el analizador en la caja de texto así como tambien mostrará las instrucciones recopiladas. 

![Analizar](https://i.ibb.co/CmBQH5f/MU-Boton-analizar.png)

Boton Errores:

La funcionalidad de este boton rádica en que muestra los caractéres no reconocidos por el analizador, luego los mostrará en el cuadro de texto en formato json en la cual desplegara la cantidad de errores y el tamaño del archivo tendrá un tamaño variable según así lo requiera.

![Errores](https://i.ibb.co/KrtP7Nt/MU-Boton-errores.png)

Boton Reportes:

La funcionalidad de este boton es mostrar los diagramas de las operaciones anteriormente analizadas, lo cual lo hará por medio de arboles binarios, esto generará un archivo llamado Resultados_202110511  

![Reportes](https://i.ibb.co/cbNDMJ8/MU-Boton-Reporte.png)

Los diagramas mostrados tendrán el siguiente formato y estos se guardarán en el mismo directorio del Proyecto 

![Diagramas](https://i.ibb.co/6RTbZ6R/MU-Diagramas.png)


Este fue el manual de Usuario esperamos que sea de mucha ayuda para tu comprensión sobre la funcionalidad del programa así que mucha suerte!