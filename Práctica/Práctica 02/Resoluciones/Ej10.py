nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]



#Función que recibe un caracter como parametro,
# y retorna si es una letra o no.
def esLetra(char):
    acentos = ["á", "é", "í", "ó", "ú"]
    esAcento = False

    #Determina si el caracter es una letra con acento.
    for elem in acentos:
        if char.lower() == elem:
            esAcento = True
    
    return (char.lower() >= "a" and char.lower() <= "z") or esAcento


#Función que genera y retorna una lista con los nombres de
#todos los alumnos contenidos en el string "nombres".
def generarListaNom():
    #Defino una lista vacía y un string vacío.
    listaNom = []
    nom = ""

    #Para cada caracter del string "nombres"...
    for char in nombres:    
        #...Si el caracter es una letra...
        if esLetra(char):
            #...Se concatena en "nombre".
            nom += char
        #...Si no es una letra, y "nombre" no está vacío...
        elif nom != "":
            #...Agrego el nuevo "nombre" al final de la lista,
            # y vacío el contenido "nombre" para el siguiente nombre.
            listaNom.append(nom)
            nom = ""

    return listaNom


#Funcion que genera y retorna una estructura tipo diccionario,
#que contiene tuplas donde cada tupla representa a un estudiante
#y sus notas.
def generarEstructura():
    #Genero una lista que contiene los
    #nombres de todos los estudiantes.
    listaNombres = generarListaNom()    

    #Itero sobre las listas de notas en paralelo, generando
    #una tupla por cada iteración y agregandola a una lista.
    tuplaNotas = list(zip(notas_1, notas_2))

    #Con las dos listas generadas anteriormente, genero un
    #diccionario donde se asocia un nombre de estudiante con
    #un par de notas, iterando en paralelo sobre ambas listas.
    dictAluNotas = dict(zip(listaNombres, tuplaNotas))
    
    return(dictAluNotas)



#Funcion lambda que calcula el promedio entre dos parámetros.
promedio = lambda x, y: (x + y) / 2    


#Funcion que recorre un diccionario que recibe como parámetro,
#y calcula e imprime el promedio de las notas para cada
#estudiante contenido en la estructura.
def promPorAlumno(notasAlumnos):
    print('\n-- PROMEDIOS POR ESTUDIANTE --\n')

    #Para cada estudiante en el diccionario...
    for alumno in notasAlumnos:
        #...Calculo e imprimo el promedio de sus notas junto
        #con el nombre del estudiante.
        aluPromedio = promedio(notasAlumnos[alumno][0], notasAlumnos[alumno][1])                 
        print(f"{alumno}: {aluPromedio}\n")


#Funcion que recorre un diccionario que recibe como parámetro,
#y calcula e imprime el promedio total entre todos los estudiantes
#del curso.
def promCurso(notasAlumnos):
    #Defino una lista vacía.
    listaProm = []

    #Para cada estudiante en el diccionario...
    for alumno in notasAlumnos:
        #...Calculo el promedio de sus notas y lo agrego a la lista.
        listaProm.append(promedio(notasAlumnos[alumno][0], notasAlumnos[alumno][1]))

    #Imprimo el promedio total, totalizando todos los promedios y luego
    #dividiendo ese valor por la cantidad total de promedios en la lista.
    print(f' -- PROMEDIO DEL CURSO: \n {sum(listaProm) / len(listaProm)}\n')


#Funcion que recorre un diccionario que recibe como parámetro,
#y calcula e imprime quién es el estudiante con el promedio más
#alto del curso.
def promedioAlto(notasAlumnos):
    #Inicializo una variable entera en un valor
    #muy bajo para guardar el promedio máximo.
    promMax = -1

    #Para cada estudiante en el diccionario...
    for alumno in notasAlumnos:
        #...Calculo el promedio de sus notas.        
        aluPromedio = promedio(notasAlumnos[alumno][0], notasAlumnos[alumno][1])
        
        #Si el promedio del alumno actual es mayor que el promedio máximo...
        if(aluPromedio > promMax):
            #...Actualizo el nuevo alumno y promedio máximos.
            promMax = aluPromedio
            nombreMax = alumno

    #Imprimo los datos del alumno con promedio más alto del curso.
    print(f" -- Alumno con el promedio más alto: \n {nombreMax} - {notasAlumnos[nombreMax]} - {promMax}\n")


#Funcion que recorre un diccionario que recibe como parámetro,
#y calcula e imprime quién es el estudiante con la nota más
#baja del curso.
def notaBaja(notasAlumnos):
    #Inicializo una variable entera en un valor
    #muy alto para guardar nota más baja.
    notaMin = 9999
    
    #Para cada estudiante en el diccionario...
    for alumno in notasAlumnos:
        #...Calculo el mínimo entre sus notas.
        notaActual = min(notasAlumnos[alumno])

        #Si la nota del alumno acutal es menor que la nota mínima...
        if notaActual < notaMin:
            #...Actualizo el nuevo alumno y promedio mínimos.
            notaMin = notaActual
            nombreMin = alumno
    
    #Imprimo los datos del alumno con la nota más baja del curso.
    print(f" -- Alumno con la nota más baja: \n {nombreMin} - {notasAlumnos[nombreMin]} - {notaMin}\n")




###
###
# Programa Principal
###
###


## INCISO A ##
#Genero una estructura tipo diccionario, donde las claves son
#nombres de estudiantes, y los valores son tuplas que contienen
#dos notas.
notasAlumnos = generarEstructura()
print(notasAlumnos)

## INCISO B ##
#Llamo a una función encargada de calcular e informar los promedios
#de cada alumno. Envío el diccionario generado en el inciso A
#como parámetro.
promPorAlumno(notasAlumnos)

## INCISO C ##
#Llamo a una función encargada de calcular e informar el promedio
#total del curso. Envío el diccionario generado en el inciso A
#como parámetro.
promCurso(notasAlumnos)

## INCISO D ##
#Llamo a una función encargada de calcular e informar quién es el
#estudiante con el promedio más alto del curso.
promedioAlto(notasAlumnos)

## INCISO E ##
#Llamo a una función encargada de calcular e informar quién es el
#estudiante con la nota más baja del curso.
notaBaja(notasAlumnos)