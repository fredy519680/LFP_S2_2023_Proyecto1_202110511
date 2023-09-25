# -*- coding: utf-8 -*-
import tkinter 
from tkinter import filedialog
from collections import namedtuple
import json

archivoac = None
Token = namedtuple("Token",["value", "line", "col"])  #Tupla que nos ayudara a guardar el valor de cada Token
Errors = namedtuple("Error",["value", "linea", "col"]) #Tupla para guardar los calores de vada error

linea= 1  # variable para el conteo de las lineas
colum = 1  # variable para el conteo de las columnas
tokens = [] # vector para guardar los tokens
Errores= [] # vector para guardar los errores

def tokenstring(texto, i): #Función que convierte los string en tokens 
    token=""
    for char in texto:
        if char == '"': 
            return [token.lower(), i] #devuelve el token hasta las comillas que lo cierra y lo pone en minusculas 
        token +=char
        i+=1
    print("String no cerrado", token)

def tokennumero(texto, i): #función que vuelve token los numeros dependiendo si es entero o es decimal
    token=""
    decimal = False
    for char in texto:
        if char.isdigit(): #validar si es digito
            token += char
            i +=1
        elif char ==".": #validar si es decimal
            token+=char
            i += 1
            decimal = True
        else: 
            break
    if decimal:
        return [float(token), i] #devuelve el valor float si decimal es true
    
    return [int(token),i] #devuelve el valor int si el valor es entero

def leertexto(texto):
    global linea, colum, tokens, Errores

    i =0

    while i < len(texto): #función para leer el archivo
        char = texto[i]
        if char.isspace(): #verificar si es un espacio y dependiendo agregar valor a fila y columna
            if char== "\n":
                linea += 1
                colum = 1
            elif char == "\t":
                colum += 4
            i +=1
        elif char == '"': #Verificar si inicia una string con posible token
            string, pos = tokenstring(texto[i+1:], i) #Llama a la función para crear un token string en la posición que se encuentra leyendo y lo devuelve con posicion
            colum += len(string) + 1
            i= pos+2
            token = Token(string, linea, colum)
            tokens.append(token)#agregar el token al vector de tokens
        elif char in ["{", "}", "[", "]", ",", ":"]: #verificar si es uno de los caracteres del archivo json 
            colum += 1
            i+= 1
            token = Token(char, linea, colum)
            tokens.append(token)#agregar el token al vector de tokens
        elif char.isdigit():# verificar si el char es un número
            numero, pos = tokennumero(texto[i:],i)# llamar a la función para convertir el numero en un token y devolverlo con la posición 
            colum += pos-i
            i = pos
            token = Token(numero, linea, colum)
            tokens.append(token)#agregar el token de número al vector de tokens
        else:
            print( #imprime el error en la consola 
                "Error: caracter desconocido:",
                char,
                "en linea:",
                linea,
                "columna:",
                colum,
            )
            error = Errors(char,linea,colum) #guarda el error en la tupla de errores
            Errores.append(error) # agrega el error a el vector de errores 
            i += 1
            colum += 1

def get_instruction():# esta función sirve para evualuar la cadena de tokens y convertirlas en instrucciones utiles 
    global tokens
    operacion = None
    value1 = None
    value2 = None
    while tokens:
        token = tokens.pop(0)
        if token.value == "operacion":
            tokens.pop(0)
            operacion = tokens.pop(0).value
        elif token.value == "valor1":
            tokens.pop(0)
            value1 = tokens.pop(0).value
            if value1 == "[":
                value1 = get_instruction()
        elif token.value == "valor2":
            tokens.pop(0)
            value2 = tokens.pop(0).value
            if value2 == "[":
                value2 = get_instruction()
        else:
            pass

        if operacion and value1 and value2:
            return [operacion, value1, value2]
        elif operacion and operacion in ["seno"] and value1:
            return [operacion, value1]
    return None

def create_instructions(): # esta función crea las instrucciones y llama la función que las evalua para guardarla en un vector de instrucciones
    global tokens
    instrucciones = []
    while tokens:
        instruccion = get_instruction()
        if instruccion:
            instrucciones.append(instruccion)
    return instrucciones


def abrir_archivo():
    global archivo_actual
    archivo = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")]) #variable que guarda la ruta de archivo tipo json
    if archivo:
        with open(archivo, "r") as f: #abrir el archivo 
            contenido = f.read()
            cajatexto.delete(1.0, tkinter.END)   #borrar el contenido de la caja de texto 
            cajatexto.insert(tkinter.END, contenido) #insertar el contenido
        archivo_actual = archivo

def guardar_archivo():
    global archivo_actual
    if archivo_actual: #verificar si el archivo ya tiene una ruta
        with open(archivo_actual, "w") as f:
            contenido = cajatexto.get(1.0, tkinter.END)
            f.write(contenido) #guardar el contenido con el mismo nombre
            print("El archivo se guardo exitosamente")
    else:
        print("no existe ruta para guardar el archivo")
    
def guardar_como():
    archivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")]) #variable que guarda la ruta del archivo con su nombre
    if archivo:
        with open(archivo, "w") as f:
            contenido = cajatexto.get(1.0, tkinter.END)
            f.write(contenido) #guardar el contenido en el archivo

def get_cajatexto(): #funcion para obtener la caja del texto 
    contenido = cajatexto.get(1.0, tkinter.END)
    return contenido

def borrar_cajatexto(): #función para borrar el texto
    cajatexto.delete(1.0, tkinter.END)
    archivoac = None

def analizar_archivo():
    entrada =  cajatexto.get(1.0, tkinter.END)
    leertexto(entrada)
    borrar_cajatexto()
    for i in tokens:
        tf = f">>> {i}\n"
        cajatexto.insert(tkinter.END, tf)

def guardar_json(): #función para guardar el archivo json que se encuentra en la caja de texto 
    contenido_json = cajatexto.get("1.0", "end")  

    try:
        datos = json.loads(contenido_json) #guarda el contenido de la caja de texto en una variable
        with open("errores.json", "w") as archivo:
            json.dump(datos, archivo, indent=4) # guarda el contenido en un archivo json
            print("Archivo JSON guardado correctamente.")

    except json.JSONDecodeError as e:
        print("Error al analizar el JSON:", e)

def mostrar_errores(): #funcion para mostrar los errores y los caracteres desconocidos 
    global Errores
    borrar_cajatexto() #borrar el contenido de la caja de tecto
    secciones = [] #aquí se guardaran las secciones que se irán agregando 
    json_data = { #Los datos del archivo jason
    "errores": secciones #Estas son las secciones que iran mostrandose conforme se vayan agregando
    }
    cont=1
    for i in Errores:
        nueva_seccion = { #Sección nueva que se crea con los datos del error almacenado en el vector de errores
        "No": cont,
        f"Descripción": {
            "lexema": f"{i.value}",
            "tipo": f"error lexico",
            "columna": i.linea,
            "fila": i.col
        }
    }
        secciones.append(nueva_seccion)# se agrega la nueva sección a los datos json
        cont +=1

        #tf = f">>>   {i.value}\n"
        #cajatexto.insert(tkinter.END, tf)
    cadena_json = json.dumps(json_data, indent=4, ensure_ascii=False)
    cajatexto.insert(tkinter.END, cadena_json) # se insertan los datos en la caja de texto donde se pueden visualizar
    guardar_json() #se llama a la función guardar archivo json para guardar el archivo y crearle nombre 


        

ventana = tkinter.Tk() # Ventana principal en donde estarán los botones y caja de texto
ventana.title("Analizador Léxico")
ventana.geometry("1000x700")
ventana.configure(bg="gray25")

superior = tkinter.Frame(ventana, bg="blue")# un frame superior en el cual se colocaran los botones para su distinción
superior.pack(fill="both", expand=True)

superior.grid_rowconfigure(0, weight=1)
superior.grid_columnconfigure(0, weight=1)

botones = tkinter.Frame(superior, bg="blue")# otro frame para poder colocar los botones de manera dentrada en la ventana
botones.grid(row=0, column=0, sticky="nsew")

boton1 = tkinter.Menubutton(botones, text="Archivo", width=10 , height= 2, bg="lightgray")# Boton con menu desplegable para el manejo de archivos
boton1.menu = tkinter.Menu(boton1, tearoff=0)
boton1["menu"]= boton1.menu 
boton1.menu.add_command(label="Abrir", command=lambda: abrir_archivo())#Boton con funciones
boton1.menu.add_command(label="Guardar", command=lambda: guardar_archivo())#Boton con funciones
boton1.menu.add_command(label="Guardar Como", command=lambda: guardar_como())#Boton con funciones
boton1.menu.add_separator()
boton1.menu.add_command(label="Salir", command=ventana.quit)

boton2 = tkinter.Button(botones, text="Analizar",width=10 , height= 2, bg="lightgray", command=lambda: analizar_archivo())#Boton con funciones
boton3 = tkinter.Button(botones, text="Errores",width=10 , height= 2, bg="lightgray", command=lambda: mostrar_errores())#Boton con funciones
boton4 = tkinter.Button(botones, text="Reporte",width=10 , height= 2, bg="lightgray", command=lambda: borrar_cajatexto())#Boton con funciones

boton1.pack(side="left", padx=50)#colocar los botones con el comando pack y una separación entre ellos
boton2.pack(side="left", padx=50)
boton3.pack(side="left", padx=50)
boton4.pack(side="left", padx=50)

inferior = tkinter.Frame(ventana, bg="white")#Frame inferior en donde se colocará la caja de texto
inferior.pack(fill="both", expand=True)


cajatexto = tkinter.Text(inferior,borderwidth=7,relief="solid", font=("Arial", 12))#caja de texto configurada y colocada con el comando pack 
cajatexto.pack(fill="both", expand=True)
cajatexto.config(highlightbackground="gray")


ventana.mainloop() # instrucción que manda a llamar a la venta