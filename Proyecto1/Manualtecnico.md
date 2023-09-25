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
## Manual Tecnico 
Este manual Técnico tiene como funcionalida dar a entender la lógica de programación detrás del mismo funcionamiento, con un lenguaje más enfocado a programadores y personas que tengán el interés sobre entender el código o en algún futuro darl mantenimiento a esta aplicación o mejorarla. 

Código con Tkinter para la interfaz gráfica :
Para la creación de la interfaz gráfica hicimos uso de la librería de tkinter la cual tuvimos que importar con la instrucción import tkinter, Luego de estotuvimos que programar la ventana con cada uno de sus widgets y la caja de texto con el código comentado que ven acontinuación. 

![tkinter](https://i.ibb.co/zPpfYvR/MT-Interfaz-tkinter.png)

Funciones de manejo de  archivo: 
Como ya sabemos necesitamos hacer que los botones funciones y para el boton de archivo creamos funciones para poder ser llamadas cuando presionaramos el boton y las funciones son las siguiente. 

-abrir_archivo: Esta opcion nos abre el explorador de archivos y nos permite escoger cualquier archivo de tipo json

-guardar_archivo: Esta opción guarda el archivo con el mismo nombre con el que se abrió 

-guardar_como: Guardar como nos permite guardar el archivo en formato json con el nombre que nosotros querramos 
 

![manejoarchivo](https://i.ibb.co/t4RZHf0/MT-Funciones-archivo.png)


Funciones para la caja de texto: 

Estas son funciones que nos serviran para el manejo del contenido de la caja de texto, en la cual tendremos la función de obtener la cadena de texto dentro de la caja de texto y tambien la función para borrar el contenido en la misma. 

![funciones cajatexto](https://i.ibb.co/k1GpLbR/MT-Funciones-caja-texto.png)

Funciones Para los tokens:

Para volver tokens los valores de la cadena necesitamos 2 funciones que reconozcan los las palabras y los números.

Función token string: Esta función lee el texto desde donde inicia la comilla hasta donde finaliza y vuelve el conjunto de caracteres en un token
funcion token numero: Esa función lee los caracteres númericos en el texto y los vuelve token dependiendo si son enteros o decimales 

![Crear tokens](https://i.ibb.co/1YgCP26/MT-Funciones-crear-tokens.png)

Función para leer el texto:

La funcionalidad de esta se basa en leer el texto caracter por caracter y dependiendo de los caracteres si los reconoce llama a las funciones de crear tokens de string o de numero, así como tambien guarda todos aquellos token que son reconocidos por el analizador y los que los toma como errores y los agrega a la lista de errores

![Errores](https://i.ibb.co/Zg8W0QS/MT-Funcione-leertexto.png)

Funciónes para instrucciones:

Estas funciones nos ayudaran a eliminar los caracteres extras que tenemos en la lista de tokens y evaluaran el tipo de operación y los valores necesarios para que realizar dicha operación, asi como la función que crea las instrucciones que las almacena en un vector donde estaran las isntrucciones condensadas

![Reportes](https://i.ibb.co/8sTrxX3/MT-Funcion-crear-instrucciones.png)

Funciones para guardar el arhcivo json y mostrar errores:

En la función de guardar el archivo json esta nos permitirá guardar el archivo json que se encuentre en la caja de texto y verificara si el archivo en formato json es valido 

En la función de mostrar errores borrará el contenido de al caja de texto y agregara las secciones a los datos json que se mostraran para poder crear un archivo con la cantidad que se desee de errores y no se pierda el formato de tipo json. 

![Diagramas](https://i.ibb.co/6WR5bsG/MT-Funcion-guardar-jsonerrores.png)


Este fue el manual técnico esperamos que si algun programador o persona que revise el código pueda entender con claridad la funcionalidad del mismo gracias a los comentarios y la explicación de los mismos. 