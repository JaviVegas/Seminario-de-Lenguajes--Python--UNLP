import json, csv
import  clases 
import random

def obtengoDatos(nombreArchivo):

    if nombreArchivo.endswith("jcson"):
        archi = open(nombreArchivo, "r")
        datos=json.load(archi)
        archi.close()
    elif nombreArchivo.endswith("csv"):
        archi = open(nombreArchivo, "r")
        csvreader = csv.reader(archi, delimiter=',')
        linea1 = next(csvreader)
        linea2 = next(csvreader)
        datos = dict(zip(linea1, linea2))
        archi.close()
    else:
        datos = {}
    return datos


archivos = ["datos.json", "datos.csv"]
archi = random.choice(archivos)
datosBandas = obtengoDatos(archi)

banda = clases.Banda(datosBandas['nombre'], datosBandas["genero"])

lista = []
try:
    for i in range(datosBandas["cant_integrantes"]):
        nom = input("Ingresá un integrante")
        lista.append(nom)

    banda.integrantes = lista
    print(banda)
    print("FIN DEL PROGRAMA")

except TypeError:
    print("Ocurrió un error durante la ejecución. Por favor, vuelva a intentarlo.")
